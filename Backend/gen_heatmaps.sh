#!/bin/bash
# -!- encoding:utf8 -!-

# ------------------------- CONFIGURATION

DEBUG=0

# ------------------------- SCRIPT

MODE=${1}
PRECISION=${2}
METHOD=${3}
ELEMENT=${4}

GRIDS=("lescheres" 
    "neyron" 
    "jons" 
    "stgermain" 
    "charbonnieres" 
    "genay" 
    "givors" 
    "montluel" 
    "cailloux" 
    "craponne" 
    "fontainesstm" 
    "grigny" 
    "standeol" 
    "lyon5" 
    "anse" 
    "genas" 
    "solaize" 
    "mions" 
    "villetteda" 
    "vaulx" 
    "stromain" 
    "brindas" 
    "civrieux" 
    "caluire" 
    "dagneux" 
    "chaponnay" 
    "stcyr" 
    "lyon2" 
    "grezieu" 
    "lyon6" 
    "stquentin" 
    "quincieux" 
    "montagny" 
    "unnamed" 
    "stpierredec" 
    "stsymphorien" 
    "fleurieu" 
    "stmaurice" 
    "nievroz" 
    "pierrebenite" 
    "massieux" 
    "latour" 
    "marennes" 
    "francheville" 
    "neuville" 
    "amberieux" 
    "rillieux" 
    "stpriest" 
    "limonest" 
    "echalas" 
    "serezin" 
    "corbas"
    "simandres" 
    "balan" 
    "stdidier" 
    "sathonayv" 
    "decines" 
    "oullins" 
    "montanay" 
    "stbonnet" 
    "couzon" 
    "albigny" 
    "chassagny" 
    "stgenislaval" 
    "lyon7" 
    "ecully" 
    "grenay" 
    "mionnay" 
    "chasse" 
    "trevoux" 
    "lyon8" 
    "dommartin" 
    "thil" 
    "beynost" 
    "tassin" 
    "loiresurr" 
    "irigny" 
    "marcyle" 
    "fontainesss" 
    "sathonayc" 
    "lyon9" 
    "laboisse" 
    "curis" 
    "venissieux" 
    "champagne" 
    "communay" 
    "vourles" 
    "rochetaillee" 
    "steconsorce" 
    "feyzin" 
    "janneyrias" 
    "marcilly" 
    "poleymieux" 
    "lyon1" 
    "lissieu" 
    "miribel" 
    "stgenisleso" 
    "millery" 
    "stfons" 
    "stlaurentdem" 
    "colombier" 
    "stefoy" 
    "dardilly" 
    "pusignan" 
    "lyon3" 
    "charly" 
    "chassieu" 
    "lyon4" 
    "meyzieu" 
    "chasselay" 
    "vernaison" 
    "jonage" 
    "collonges" 
    "tramoyes" 
    "brignais" 
    "lucenay" 
    "bron" 
    "lamulatiere" 
    "ternay" 
    "villeurbanne")

CRITERIAS=("le_enseignement" 
    "pit_hebergement_collectif" 
    "le_culte" 
    "tcl" 
    "pit_commerce_et_service" 
    "pit_hotellerie_plein_air" 
    "le_sante" 
    "le_deplacement" 
    "pit_patrimoine_naturel" 
    "pit_patrimoine_culturel" 
    "le_administration pit_hotellerie" 
    "pit_hebergement_locatif" 
    "pit_restauration" 
    "le_sport" 
    "velov" 
    "pit_equipement" 
    "pit_degustation"
    "bruit"
    "le_urgence")

let "CRITERIAS_LEN = ${#CRITERIAS[@]} + 1"
let "GRIDS_LEN = ${#GRIDS[@]}"
let "TOTAL = ${CRITERIAS_LEN} * ${GRIDS_LEN}"

# Verification des inputs
if [[ "${MODE}" == "help" ]]; then
    echo "Usage :"
    echo "  + ./gen_heatmaps.sh grid <int:precision> <str:method> <str:gridname>"
    echo "  + ./gen_heatmaps.sh criteria <int:precision> <str:method> <str:criteria>"
    echo "  + ./gen_heatmaps.sh all <int:precision> <str:method>"
    exit
fi
if [ "${MODE}" != "grid" ] && [ "${MODE}" != "criteria" ] && [ "${MODE}" != "all" ]; then
    echo "Wrong parameter ! Type './gen_grids.sh help' to get some help."
    exit
fi
if [[ "${PRECISION}" == "" ]]; then
    PRECISION="100"
fi
METHOD=$(echo "${METHOD}" | tr [:lower:] [:upper:])
METHOD_LW=$(echo "${METHOD}" | tr [:upper:] [:lower:])
if [[ "${METHOD}" != "QCGR" ]]; then
    METHOD="FGR"
fi

# Fonction

gen_grid () {
    if [[ "${DEBUG}" == "0" ]]; then
        ./maintenance.py heatmap reduce ${1} ${PRECISION} ${METHOD}
    else
        echo "./maintenance.py heatmap reduce ${1} ${PRECISION} ${METHOD}"
    fi
}

gen_heatmap () {
    if [[ "${DEBUG}" == "0" ]]; then
        ./maintenance.py heatmap gen ${1}_red_${PRECISION}_${METHOD_LW} ${2}
    else
        echo "./maintenance.py heatmap gen ${1}_red_${PRECISION}_${METHOD_LW} ${2}"
    fi
}

# Main loops

i=0
if [[ "${MODE}" == "all" ]]; then
    for grid in ${GRIDS[@]}; do
        gen_grid ${grid} ${PRECISION} ${METHOD}
        for criteria in ${CRITERIAS[@]}; do
            i=$((i+1))
            gen_heatmap ${grid} ${criteria}
            echo "[BASH]> overall progress : ${i}/${TOTAL}"
        done
    done
elif [[ "${MODE}" == "grid" ]]; then
    for criteria in ${CRITERIAS[@]}; do
        i=$((i+1))
        gen_heatmap ${ELEMENT} ${criteria}
        echo "[BASH]> overall progress : ${i}/${CRITERIAS_LEN}"
    done
elif [[ "${MODE}" == "criteria" ]]; then
    for grid in ${GRIDS[@]}; do
        i=$((i+1))
        gen_heatmap ${grid} ${ELEMENT}
        echo "[BASH]> overall progress : ${i}/${GRIDS_LEN}"
    done
fi

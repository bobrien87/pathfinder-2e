---
type: creature
group: ["Amphibious", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Amoeba"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Amphibious"
trait_02: "Mindless"
trait_03: "Ooze"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4; [[Motion Sense]] (precise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +6, Stealth +3"
abilityMods: ["+3", "-2", "+2", "-5", "+0", "-5"]
abilities_top:
  - name: "Motion Sense"
    desc: "A giant amoeba can sense nearby creatures through vibration and air or water movement."
  - name: "Weak Acid"
    desc: "A giant amoeba's acid damages only organic material-not metal, stone, or other inorganic substances."
armorclass:
  - name: AC
    desc: "8; **Fort** +7, **Ref** +3, **Will** +5"
health:
  - name: HP
    desc: "45; **Immunities** acid, critical hits, precision, unconscious, visual; **Weaknesses** slashing 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pseudopod +8 (`pf2:1`) (unarmed), **Damage** 1d6 acid plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[1d4[bludgeoning],1d4[acid]]{1d4 bludgeoning plus 1d4 acid}, DC 17 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Envelop"
    desc: "`pf2:3` **Requirements** The giant amoeba begins its turn with a target its size or smaller [[Grabbed]] <br>  <br> **Effect** The giant amoeba maintains the [[Grab]] and extends pseudopods to surround the creature and pull it inside the amoeba's body. This thereafter has the same effect as if the amoeba had [[Engulfed]] the creature (DC 17, 1d6 acid damage, `act escape dc=17`, Rupture 3)."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These blobs of nearly transparent protoplasm are identical in form and behavior to the microscopic creatures from which they have evolved, except their outlandish size makes them all the more dangerous. Unlike slimes, puddings, and other deadly oozes, giant amoebas have an outer membrane that contains their internal structures, making them more susceptible to slashing weapons than their amorphous kin. However, this membrane is also extremely flexible and permeable, allowing them to surround prey and absorb it, suffocating and slowly digesting it in the amoeba's acidic fluids.

```statblock
creature: "Giant Amoeba"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

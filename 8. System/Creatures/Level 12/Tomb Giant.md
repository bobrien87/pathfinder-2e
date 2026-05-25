---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tomb Giant"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+25; [[Darkvision]], [[Lifesense]] (imprecise) 60 feet"
languages: "Common, Jotun, Necril"
skills:
  - name: Skills
    desc: "Athletics +25, Medicine +25, Occultism +23, Religion +25, Stealth +21"
abilityMods: ["+7", "+3", "+6", "+3", "+7", "+4"]
abilities_top:
  - name: "Dooming Touch"
    desc: "The tomb giant's claws carry the accursed power of their foul gods. A creature hit by the tomb giant's claw Strike becomes [[Doomed]] 1."
armorclass:
  - name: AC
    desc: "32; **Fort** +22, **Ref** +19, **Will** +25"
health:
  - name: HP
    desc: "255; void healing; **Immunities** death effects"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scythe +27 (`pf2:1`) (deadly d10, magical, reach 10 ft., trip), **Damage** 2d10+13 slashing"
  - name: "Melee strike"
    desc: "Claw +26 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 3d6+13 slashing plus [[Dooming Touch]]"
  - name: "Ranged strike"
    desc: "Rock +24 (`pf2:1`) (brutal, range 120 ft.), **Damage** 3d8+13 bludgeoning"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32, attack +0<br>**3rd** [[Bind Undead]]<br>**1st** [[Harm]]"
abilities_bot:
  - name: "Font of Death"
    desc: "`pf2:3` The tomb giant turns the spiritual tide on a creature that has just died, temporarily transforming it into a volatile vessel powered by the Void. The tomb giant touches a creature that died within the past 24 hours, infusing its flesh and bone with void energy. Once during the next hour, the tomb giant can spend a single action (from any distance) to release this void from the corpse in an explosion that deals @Damage[10d8[void]|options:area-damage] damage in a @Template[type:burst|distance:15] (DC 32 [[Fortitude]] save); if not released before the end of the hour, the energy dissipates harmlessly. The tomb giant can't use Font of Death while a previous corpse remains infused."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Masters of mausoleums and keepers of crypts, the dread creatures called tomb giants are anathema to all living beings, but especially so to other types of giants. Long ago, so the legends say, tomb giants sold their souls in exchange for unfathomable power over the undead. Tomb giants construct massive gothic settlements in haunted valleys and on forsaken hillsides, far enough away from the societies of smaller people that they remain relatively undisturbed, but close enough that they can raid the graveyards of nearby villages with impunity. Elder tomb giants enjoy the thrill of subduing, slaying, and reanimating their fellow giants. A tomb giant views its mortal life as only one part of its existence. After death, most tomb giants are reanimated as undead, who then continue to practice their necromantic arts.

Spread across the world, giants are as diverse as the isolated places they inhabit. A giant makes a big impression on the local environment, especially on smaller and weaker creatures.

```statblock
creature: "Tomb Giant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

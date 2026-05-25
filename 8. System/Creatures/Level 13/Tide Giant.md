---
type: creature
group: ["Amphibious", "Giant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tide Giant"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Amphibious"
trait_02: "Giant"
trait_03: "Humanoid"
trait_04: "Water"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Low-Light Vision]]"
languages: "Common, Jotun"
skills:
  - name: Skills
    desc: "Athletics +27, Nature +21, Survival +23"
abilityMods: ["+8", "+6", "+6", "+0", "+4", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "33; **Fort** +23, **Ref** +25, **Will** +21"
health:
  - name: HP
    desc: "250; **Resistances** fire 10"
abilities_mid:
  - name: "Cloak of High Tide"
    desc: "10 feet. <br>  <br> Elemental water magic ebbs and flows into a tide giant. At the start of each of the giant's turns in combat, their cloak of high tide automatically activates if it's inactive or ends if it's already active. Any creature other than a tide giant that enters or starts its turn in the aura while it's active regains @Damage[5[healing,vitality]|shortLabel] HP; this is a healing vitality effect, and a creature can benefit from it only once per round. When active, the cloak appears as a magical, flowing cloak of seafoam that billows from the tidal giant's shoulders and the back of their limbs. The cloak is inactive when the tide giant isn't in combat."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Trident +28 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d8+14 piercing"
  - name: "Melee strike"
    desc: "Trident +26 (`pf2:1`) (magical, thrown 20), **Damage** 2d8+14 piercing"
  - name: "Melee strike"
    desc: "Fist +27 (`pf2:1`) (agile, nonlethal, reach 10 ft., unarmed), **Damage** 2d4+14 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 33, attack +0<br>**5th** [[Control Water]]"
abilities_bot:
  - name: "Blood Tide"
    desc: "`pf2:2` The tide giant Swims, or Swims twice if their cloak of high tide is active. Holding out their trident, they slash those they pass, dealing @Damage[2d8[piercing],2d6[bleed]] damage (DC 24 [[Reflex]] save) to each enemy the giant moves within 10 feet of during their movement. Each creature can be affected only once during a single use of Blood Tide."
  - name: "Tine and Tide"
    desc: "`pf2:2` A wave blasts from the giant's trident in a @Template[type:cone|distance:15] or a @Template[type:burst|distance:5] within 100 feet. If the giant's cloak of high tide is active, this is a @Template[type:cone|distance:30] or a @Template[type:burst|distance:10]. Each creature in the area takes @Damage[9d8[bludgeoning]|options:area-damage] damage with a DC 33 [[Reflex]] save."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

On secluded beaches where the waves lap across pristine, untouched sands, tide giants dwell in solitude at the shore. They aim to live in quiet serenity, appreciating the beauty that surrounds them. Tide giants thrive on lounging on the sand, living slow while taking in the sights, sounds, and smells of the shore, all while enjoying bowls of juice and rum. Many live by the philosophy that their precious and sacred connection to the magic of the sea is deepened by enjoying the water, such as by watching the sun reflect off the waves cresting the shore. Interruptions, trespassers, and other surprises upset tide giants' calm massively, turning their placid attitude into an enraged hurricane.

Spread across the world, giants are as diverse as the isolated places they inhabit. A giant makes a big impression on the local environment, especially on smaller and weaker creatures.

```statblock
creature: "Tide Giant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

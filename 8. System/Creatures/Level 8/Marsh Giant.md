---
type: creature
group: ["Amphibious", "Giant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Marsh Giant"
level: "8"
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
    desc: "+16; [[Low-Light Vision]]"
languages: "Aklo, Common, Jotun, Thalassic"
skills:
  - name: Skills
    desc: "Athletics +18, Intimidation +15, Nature +15, Religion +17"
abilityMods: ["+6", "+3", "+4", "+0", "+3", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "27; **Fort** +18, **Ref** +13, **Will** +17"
health:
  - name: HP
    desc: "150"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Gaff +20 (`pf2:1`) (magical, reach 10 ft., trip, versatile p), **Damage** 2d6+14 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 2d6+14 bludgeoning"
  - name: "Ranged strike"
    desc: "Spit +20 (`pf2:1`) (primal, water), **Damage** 5d6 bludgeoning"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 23, attack +13<br>**5th** [[Mariner's Curse]]<br>**2nd** [[Augury]], [[Mist]]"
abilities_bot:
  - name: "Drowning Hook"
    desc: "`pf2:1` **Requirements** A creature is [[Prone]] within the marsh giant's reach <br>  <br> **Effect** The marsh giant uses its gaff to push the creature down as water bubbles up below it. The target becomes submerged in water until they are no longer prone and must hold their breath if they cannot breathe water. They take 4d6 bludgeoning damage (DC 23 [[Fortitude]] save) and lose 3 rounds worth of air if they fail the save."
  - name: "Twist the Hook"
    desc: "`pf2:2` The marsh giant makes a melee Strike with its gaff. If it hits, it twists and yanks the gaff to knock the target [[Prone]] and create an awful wound, dealing 2d6 persistent,bleed damage to the creature."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Dwellers of brackish coastal salt marshes and fetid bogs and swamps, marsh giants appear hideous to most airbreathers, with fishlike mouths, slimy graygreen skin, and dark, beady eyes. They prefer to eat the flesh of those they slay in battle, including other marsh giants, and guzzle stagnant water from cauldrons or directly from their swampy homes.

Marsh giant clans are insular, with each clan dedicating itself to zealous worship of a sea-dwelling deity, demon lord, or stranger entity. Whatever forces call to the marsh giants sometimes ensnare boggards and ogres as well, gathering in grim worship. Rather than favor these humanoid hangerson, marsh giants lavish attention on favored pets: krooths, giant octopuses, or primeval creatures like dinosaurs and the crocodilian deinosuchuses.

Barely topping 11 feet tall and 1,000 pounds, marsh giants are small for giants but make up for their stature with their zealotry.

Giants are massive humanoid creatures who live in remote regions throughout the world. They vary widely but are united in their hunger, requiring sustenance of their own element along with the feasts one would expect from such a massive humanoid. Although a simple matter for some giants, more esoteric types find this need a harsh reality. While a massive fistful of ice or snow alongside their meal will satisfy a frost giant, shadow giants hunger for the coagulated shadows of the Netherworld.

```statblock
creature: "Marsh Giant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

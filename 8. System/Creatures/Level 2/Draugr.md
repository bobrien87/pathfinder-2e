---
type: creature
group: ["Undead", "Water"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Draugr"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Undead"
trait_02: "Water"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Common (Can't speak any language)"
skills:
  - name: Skills
    desc: "Athletics +10, Stealth +8"
abilityMods: ["+4", "+2", "+3", "-1", "+1", "+1"]
abilities_top:
  - name: "Grotesque Gift"
    desc: "A draugr's attacks spatter their targets with rancid flesh and rotting seaweed. A creature damaged by a draugr's Strike must succeed at a DC 15 [[Fortitude]] save or become [[Sickened]] 1 ([[Sickened]] 2 on a critical failure)."
armorclass:
  - name: AC
    desc: "17 void healing; **Fort** +11, **Ref** +6, **Will** +7"
health:
  - name: HP
    desc: "35; **Immunities** bleed, death effects, disease, paralyzed, poison, unconscious; **Weaknesses** vitality 5; **Resistances** fire 3"
abilities_mid:
  - name: "The Sea's Revenge"
    desc: "A creature that slays a draugr is subjected to a [[Mariner's Curse]] spell with a DC 17 [[Will]] save. The curse ends if the draugr is buried in a calm sea or after 1 week passes."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greataxe +10 (`pf2:1`) (sweep), **Damage** 1d12+4 slashing plus [[Grotesque Gift]]"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile), **Damage** 1d4+4 slashing plus [[Grotesque Gift]]"
spellcasting: []
abilities_bot:
  - name: "Swipe"
    desc: "`pf2:2` The draugr powers their hate into attacking as many foes as possible. The draugr makes a melee Strike and compares the attack roll result to the AC of up to two foes, each of whom must be within its melee reach and adjacent to each other. Roll damage only once and apply it to each creature hit. A Swipe counts as two attacks for the draugr's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The risen corpses of sailors who died at sea, known as draugrs, reek of rot and decay from the briny deep. Their eyes glow with ghastly green light, and rotting seaweed, barnacles, and dead sea creatures cling to their bodies. Draugrs can't speak, but they express their malicious emotions with gurgles, as though they were eternally drowning with lungs full of water. They desire little more than to attack living creatures, especially those who sail the sea. Even when they go upon land, draugrs often drag the corpses of those they strike down back to the water, populating the depths with even more dead.

Draugrs rise in the haunted places of the sea, where restless spirits, swells of void energy, or supernatural storms deliver death. A corpse might rest at the bottom of the sea for some time before awakening as a draugr. Collecting detritus and organisms, the body becomes increasingly disgusting before it finally rises. Proximity to intelligent life can expedite this process, and an underwater explorer who happens upon a shipwreck might cause a body to suddenly return to unlife as a draugr. These undead don't take intrusions lightly, especially upon their place of death.

Though hateful of the living, draugrs are susceptible to reminders of their lives as mariners. In particular, a well-performed sea shanty or call-and-response work song might cause a draugr to become lost in reverie for a moment. The creatures have even been witnessed moaning along, unable to sing the words but providing haunting accompaniment. The lull rarely lasts long, though, as the beauty of the song quickly becomes a reminder of the tragedy that befell the draugr, reaffirming their desire for blood and death.

More powerful draugrs with burning red eyes are called draugr captains. They're 3rd-level creatures with the elite adjustment that can cast mist as an innate divine spell 3 times per day.

```statblock
creature: "Draugr"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

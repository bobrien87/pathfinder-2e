---
type: creature
group: ["Celestial", "Holy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Stone Lion"
level: "4"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Celestial"
trait_02: "Holy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Darkvision]]"
languages: "Common, Empyrean (Telepathy 60 feet)"
skills:
  - name: Skills
    desc: "Athletics +10, Intimidation +8, Religion +13, Meteorology Lore +11"
abilityMods: ["+4", "+3", "+3", "+1", "+5", "+0"]
abilities_top:
  - name: "Telepathy 60 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Anchored Soul"
    desc: "The lion is mystically bonded to its bonded vessel and must remain within 1 mile of it. Some might be further restricted to the location it guards."
  - name: "Spirit Body"
    desc: "When not Inhabiting its Vessel, the lion is incorporeal and gains resistance 5 to all damage (except force damage and damage from Strikes with the *[[Ghost Touch]]* property rune; double resistance against non-magical)."
armorclass:
  - name: AC
    desc: "21; **Fort** +11, **Ref** +9, **Will** +13"
health:
  - name: HP
    desc: "50; **Immunities** disease, paralyzed, petrified, poison"
abilities_mid:
  - name: "+1 Status to All Saves vs. Unholy"
    desc: ""
  - name: "Bonded Vessel"
    desc: "The condition of a stone lion's vessel dictates the lion's maximum Hit Point value. Undamaged, the vessel is an object with 50 Hit Points (BT 25). When the lion is in spirit form, damaging it doesn't hurt the vessel, but damaging the vessel deals an equal amount of damage to the lion. When the lion Inhabits its Vessel, they're a single target, and damage reduces the Hit Points of both the lion and the vessel. If the vessel is broken, the lion can still fight normally while inhabiting it and suffers no ill effect, but if the vessel is ever destroyed, the lion is instantly slain and can't reconstitute."
  - name: "Reconstitution"
    desc: "When the lion reaches 0 Hit Points, its spirit dissipates. If its bonded vessel is intact, the lion re-forms in this vessel after 2d4 days, fully healed. If the vessel is broken, it must first be [[Repaired]], after which the lion reforms in 3d4 days."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Ferocious Roar"
    desc: "`pf2:2` The lion makes a terrifying roar that deals @Damage[2d8[sonic]|options:area-damage] damage (DC 23 [[Fortitude]] save) to each creature in a @Template[cone|distance:20]. Creatures that fail this save become [[Frightened]] 1."
  - name: "Inhabit Vessel"
    desc: "`pf2:2` The lion touches and melds with its bonded vessel, bringing the statue to life. It can cease Inhabiting its Vessel by spending a single action, which has the concentrate trait. While Inhabiting the Vessel, it loses its fly Speed and gains <br>  <br> **Immunities** healing, nonlethal <br>  <br> **Resistances** physical 5 (except bludgeoning), <br>  <br> **Speed** 30 feet, and it gains the following Strikes: <br>  <br> - **Melee** A Jaws +14, **Damage** 2d6+7 bludgeoning plus [[Grab]]. <br>  <br> - **Ranged** A Stone Ball +13 (range increment 30 feet), **Damage** 2d4+7 bludgeoning."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Stone lions are a common sight outside of banks, temples, palaces, and even private residences. The fierce expressions affixed on their faces remind passersby to stay on their best behavior.

Stone lions remain faithful guardians of a site, regardless of whether it falls into disrepair. Even if people abandon a place, the lion remains dutiful until its statue is too worn or broken to inhabit any longer.

Stone statues of beasts can often be found paired and standing guard to either side of an entryway. While some seem like merely lifeless statues, others are far more than they appear to be. Guardian beasts ward against evil and misfortune. Some of these celestial spirits were assigned this task, while others assumed their roles out of a sense of duty. To allow them to maintain a constant presence in the material world, pious artisans carve stone vessels of the beasts in their likeness; these statues then serve as anchors for the guardian beasts' souls. Should the need arise, guardian beasts can merge with their stony form, becoming a dangerous foe with noble courage, an indomitable will, and few weaknesses.

By day, guardian beasts stay in their vessels and pretend to be inanimate. Past nightfall, they might patrol the grounds in their stone form or leave the heavy vessel behind to go where a solid body can't reach. Some take this chance to visit the dreams of individuals they favor and send them messages, notifying them of strange occurrences or warning them of incoming danger. Despite their good intentions, the dream messages from guardian beasts can be obscure, often overshadowed by the spirit's personality or strange assumptions they make due to their nature as resolute guardians.

While guardian beasts can work alone, they usually appear in bonded pairs who complement each other in nature. One could be a jokester, the other gloomy; another could be nurturing, the other strict. To make two otherwise identical-looking beasts distinct, sculptors often depict one stone animal with their young. In the case of stone lions, a common type of guardian beasts, this approach means carving stone lion cubs to accompany one of the guardians.

```statblock
creature: "Stone Lion"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

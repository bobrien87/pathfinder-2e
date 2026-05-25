---
type: creature
group: ["Celestial", "Holy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Stone Lion Cub"
level: "2"
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
    desc: "+10; [[Darkvision]]"
languages: "Common, Empyrean (telepathy 60 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +7, Religion +8, Meteorology Lore +7"
abilityMods: ["+3", "+3", "+0", "+1", "+4", "+0"]
abilities_top:
  - name: "Telepathy 60 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Anchored Soul"
    desc: "The cub is mystically bonded to its bonded vessel and must remain within 1 mile of it. Some might be further restricted to the location it guards."
  - name: "Spirit Body"
    desc: "When not Inhabiting its Vessel, the cub is incorporeal and gains resistance 3 to all damage (except force damage and damage from Strikes with the *[[Ghost Touch]]* property rune; double resistance against non-magical)."
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +7, **Will** +10"
health:
  - name: HP
    desc: "28; **Immunities** disease, paralyzed, petrified, poison"
abilities_mid:
  - name: "+1 Status to All Saves vs. Unholy"
    desc: ""
  - name: "Bonded Vessel"
    desc: "The condition of a stone cub's vessel dictates the cub's maximum Hit Point value. Undamaged, the vessel is an object with 28 Hit Points (BT 14). When the cub is in spirit form, damaging it doesn't hurt the vessel, but damaging the vessel deals an equal amount of damage to the cub. When the cub Inhabits its Vessel, they're a single target, and damage reduces the Hit Points of both the cub and the vessel. If the vessel is broken, the cub can still fight normally while inhabiting it and suffers no ill effect, but if the vessel is ever destroyed, the cub is instantly slain and can't reconstitute."
  - name: "Reconstitution"
    desc: "When the cub reaches 0 Hit Points, its spirit dissipates. If its bonded vessel is intact, the cub re-forms in this vessel after 2d4 days, fully healed. If the vessel is broken, it must first be [[Repaired]], after which the cub reforms in 3d4 days."
speed: "0 feet"
attacks: []
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17, attack +9<br>**1st** [[Detect Alignment (At Will) (Evil Only)]]"
abilities_bot:
  - name: "Inhabit Vessel"
    desc: "`pf2:2` The cub touches and melds with its bonded vessel, bringing the statue to life. It can cease Inhabiting its Vessel by spending a single action, which has the concentrate trait. While Inhabiting the Vessel, it loses its fly Speed and gains: <br>  <br> **Immunities** healing, nonlethal <br>  <br> **Resistances** physical 3 (except bludgeoning) <br>  <br> **Speed** 20 feet; and the following Strike. <br>  <br> - **Melee** A Jaws +10 (agile), **Damage** 1d6+5 bludgeoning plus [[Grab]]."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Stone lion cubs are curious, playful, and occasionally accidental mischief makers. Despite their still developing abilities, they eagerly hone their skills with make-believe missions. Many hope that they'll one day become responsible guardians like their parents.

Smaller in stature and ferocity, stone lion cubs sometimes try to guard places of smaller importance, often including facsimiles of the same kinds of structures their parents attend. They're less than dependable as guardians, as they have the attention span and rambunctious nature of children. Their parents often need to call them to heel, ordering them to stay at the parent's side as parent and child both stay motionless for the rising day.

Stone statues of beasts can often be found paired and standing guard to either side of an entryway. While some seem like merely lifeless statues, others are far more than they appear to be. Guardian beasts ward against evil and misfortune. Some of these celestial spirits were assigned this task, while others assumed their roles out of a sense of duty. To allow them to maintain a constant presence in the material world, pious artisans carve stone vessels of the beasts in their likeness; these statues then serve as anchors for the guardian beasts' souls. Should the need arise, guardian beasts can merge with their stony form, becoming a dangerous foe with noble courage, an indomitable will, and few weaknesses.

By day, guardian beasts stay in their vessels and pretend to be inanimate. Past nightfall, they might patrol the grounds in their stone form or leave the heavy vessel behind to go where a solid body can't reach. Some take this chance to visit the dreams of individuals they favor and send them messages, notifying them of strange occurrences or warning them of incoming danger. Despite their good intentions, the dream messages from guardian beasts can be obscure, often overshadowed by the spirit's personality or strange assumptions they make due to their nature as resolute guardians.

While guardian beasts can work alone, they usually appear in bonded pairs who complement each other in nature. One could be a jokester, the other gloomy; another could be nurturing, the other strict. To make two otherwise identical-looking beasts distinct, sculptors often depict one stone animal with their young. In the case of stone lions, a common type of guardian beasts, this approach means carving stone lion cubs to accompany one of the guardians.

```statblock
creature: "Stone Lion Cub"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

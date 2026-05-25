---
type: creature
group: ["Aeon", "Monitor"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vigilia"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aeon"
trait_02: "Monitor"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+24; [[Darkvision]]"
languages: "Common, Diabolic, Empyrean, Utopian"
skills:
  - name: Skills
    desc: "Athletics +20, Legal Lore +17"
abilityMods: ["+7", "+3", "+5", "+2", "+5", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "30; **Fort** +23, **Ref** +18, **Will** +20"
health:
  - name: HP
    desc: "190; **Immunities** disease, emotion, fear effects; **Resistances** electricity 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +24 (`pf2:1`) (magical, nonlethal), **Damage** 2d10+10 bludgeoning plus 1d10 electricity"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30, attack +0<br>**2nd** [[See the Unseen(Constant)]]"
abilities_bot:
  - name: "Electrical Purge"
    desc: "`pf2:2` The vigilia releases lightning from their body in a @Template[type:emanation|distance:30] dealing @Damage[4d10[electricity]|options:area-damage] damage (DC 30 [[Reflex]] save) to all creatures that aren't aeons or constructs. The vigilia is then [[Slowed]] 1 for 1 round."
  - name: "Lightning Chain"
    desc: "`pf2:1` The vigilia wraps momentary chains of electrical energy around a creature within 60 feet, dealing 2d10 electricity damage (DC 30 [[Reflex]] save). A creature that fails its save is also pulled 10 feet toward the vigilia (20 feet on a critical failure)."
  - name: "Take Prisoner"
    desc: "`pf2:1` The vigilia Interacts to pick up a Medium or smaller [[Unconscious]] creature within its reach, then Strides."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Axis's construct guardians are built in great numbers by axiomites and regularly patrol the streets of that rigidly structured metropolis. Beyond the city, a vigilia can be summoned by mortals to guard a specifc location or enforce a leader's edicts.

Although generally humanoid in form, their bodies are a loose mesh of brass strips around a crystalline core like the arbiters they're based on. Each vigilia's core is formed around a different fragment of legal text from Axis's vast libraries. This bylaw or subsection, although not necessarily important to others, forms the mystical and emotional driving force behind these sentinels.

Left to their own devices, vigilias typically enforce local laws to the best of their understanding, falling back on the labyrinthine ordinances of Axis to fll in any gaps. Although vigilias are uncomfortable making judgment calls, they're capable of doing so. That said, this discomfort frequently causes them to seek refuge in areas with the most complex and complete laws.

```statblock
creature: "Vigilia"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

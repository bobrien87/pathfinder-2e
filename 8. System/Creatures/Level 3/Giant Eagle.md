---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Eagle"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Low-Light Vision]]"
languages: "Fey, Sussuran ((Can't Speak Any Language))"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +8"
abilityMods: ["+3", "+4", "+1", "+0", "+2", "+2"]
abilities_top:
  - name: "Carry"
    desc: "A giant eagle can Fly at half Speed while it has a creature [[Grabbed]] or [[Restrained]] in its talons, carrying that creature along with it."
armorclass:
  - name: AC
    desc: "17; **Fort** +6, **Ref** +11, **Will** +9"
health:
  - name: HP
    desc: "45"
abilities_mid:
  - name: "Evasive Maneuvers"
    desc: "When a giant eagle rolls a success on a Reflex save, it gets a critical success instead."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Beak +12 (`pf2:1`) (unarmed), **Damage** 2d8+5 piercing"
  - name: "Melee strike"
    desc: "Talon +12 (`pf2:1`) (agile, unarmed), **Damage** 1d10+5 slashing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Eagle Dive"
    desc: "`pf2:2` The giant eagle [[Flies]] up to double its fly Speed in a straight line, descending at least 10 feet, and then makes a talon Strike."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

No mere animals, giant eagles have a keen intellect and a strong sense of honor. As guardians of their mountain homes, giant eagles attempt to prevent the encroachment of civilization upon wild land and the predations of wicked humanoid settlements. Giant eagles congregate within aeries holding up to a dozen members and work together to protect their domains.

Giant eagles have wingspans up to 30 feet across and weigh up to 500 pounds. A giant eagle may allow a trusted friend to ride it, but they invariably resist saddles, harnesses, or other equipment that might suggest they are mere beasts of burden. Long-lived, they take debts and oaths very seriously, often remembering slights for years and remaining slow to forgive.

Few avian creatures can match the beauty and grace of the eagle.

```statblock
creature: "Giant Eagle"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

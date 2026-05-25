---
type: creature
group: ["Fungus"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mi-Go"
level: "6"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fungus"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Low-Light Vision]], [[Tremorsense]] (precise) 30 feet"
languages: "Aklo, Common (Mi go)"
skills:
  - name: Skills
    desc: "Acrobatics +13, Arcana +15, Athletics +15, Deception +14, Medicine +17, Occultism +15, Religion +14, Stealth +13, Thievery +13"
abilityMods: ["+2", "+5", "+3", "+5", "+4", "+2"]
abilities_top:
  - name: "Clever Disguises"
    desc: "A mi-go can use Deception to [[Impersonate]] any Medium humanoid creature, although creating such a disguise takes 1 hour. It can't impersonate a specific individual with this ability."
  - name: "Sneak Attack"
    desc: "A mi-go deals an extra 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "23; **Fort** +13, **Ref** +17, **Will** +14"
health:
  - name: HP
    desc: "120; **Immunities** cold; **Weaknesses** slashing 5"
abilities_mid:
  - name: "No Breath"
    desc: "A mi-go doesn't breathe and is immune to effects that require breathing (such as an inhaled poison)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +15 (`pf2:1`) (agile, finesse, unarmed), **Damage** 2d6+4 slashing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Eviscerate"
    desc: "`pf2:1` The mi-go performs a swift and painful surgery on a creature it has [[Grabbed]] or [[Restrained]] or that is otherwise [[Immobilized]], attempting a [[Medicine]] check against the target's Fortitude DC. Regardless of the result, the target then becomes temporarily immune for 24 hours. <br> - **Critical Success** The target takes 6d6 slashing damage, is [[Slowed]] 1 for 1 round, and becomes [[Clumsy]] 1, [[Enfeebled]] 1, or [[Stupefied 1]] (the mi-go chooses) for 24 hours. <br> - **Success** The target takes 4d6 slashing damage and is slowed 1 for 1 round by the pain. <br> - **Failure** The target takes 2d6 slashing damage. <br> - **Critical Failure** The target takes no damage."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Mi-gos are both scientists and colonists, yet their extraterrestrial nature and malevolent motives color their investigations with cruelty. While their shape resembles that of an arthropod, mi-gos are in fact a highly evolved and intelligent fungus.

In mi-go society, the pursuit of secular knowledge and religious epiphany has no distinction and inspires their pursuits in tandem. They view the Outer Gods and Great Old Ones less as gods to obey and more as muses or figures of inspiration. This results in a strange blend of magic and technology they use to create bizarre organic items that are grown and spliced together as much as crafted in the traditional sense.

Mi-gos can survive the void of outer space and fly through the vacuum at incredible speeds—though these journeys still can take months within a single solar system and years to travel beyond. When they come to new planets to mine resources rare on their home worlds, they use clever disguises that mix technology and magic to appear as creatures of that world. While there, mi-gos will choose the planet's greatest minds, extract their brains, and preserve them as trophies within an eldritch cylinder.

```statblock
creature: "Mi-Go"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

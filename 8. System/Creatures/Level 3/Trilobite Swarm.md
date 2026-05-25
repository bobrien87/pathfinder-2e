---
type: creature
group: ["Animal", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Trilobite Swarm"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: "Swarm"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]], [[Wavesense]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +8, Stealth +9, Survival +7"
abilityMods: ["+1", "+4", "+3", "-5", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +10, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "30; **Immunities** swarm mind, precision; **Weaknesses** area damage 5, splash damage 5; **Resistances** bludgeoning 3, piercing 3, slashing 5"
abilities_mid: []
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Clinging Bites"
    desc: "`pf2:1` The trilobites in the swarm latch onto creatures and gnaw at them. Each enemy in the swarm's space takes @Damage[2d6[slashing]|options:area-damage] damage (DC 18 [[Reflex]] save)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Trilobites typically live in close proximity to others of their kind. On rare occasions, particularly when the most common prey around is larger than what a single trilobite can take down, they form swarms that seem to actively cooperate with each other. These swarms latch onto their prey, and the combined efforts of so many trilobites at once make escape difficult.

Often overlooked as little more than water-dwelling pests, trilobites are a varied class of arthropods found throughout the seas and oceans of Golarion. So ancient and widespread are these critters that trilobite fossils are as commonly found as living specimens. Trilobites vary wildly in both size and diet, with the largest reaching up to 28 inches long. Fossil record shows that trilobites were even more diverse and prevalent in ancient times than they are today, but their species entered a decline due to the devastation of Earthfall.

```statblock
creature: "Trilobite Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Guard Dog"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +4, Stealth +5, Survival +4"
abilityMods: ["+1", "+2", "+2", "-4", "+1", "-1"]
abilities_top:
  - name: "Pack Attack"
    desc: "The dog's Strikes deal 1d4 extra damage to creatures within the reach of at least two of the dog's allies."
armorclass:
  - name: AC
    desc: "15; **Fort** +5, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "8"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +6 (`pf2:1`) (unarmed), **Damage** 1d4+1 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The typical guard dog is loyal and beloved by many communities. Often adored as pets, they excel as protectors and trackers, and can be fearless when defending a beloved master or family member. The statistics presented below work well for numerous breeds of dog ranging from 20 to 50 pounds in weight. Wild dogs can also use these statistics, but their untamed nature makes them far more unpredictable. Feral canines are perhaps even more dangerous, for unlike their wild cousins, feral dogs often lack the instinctual fear of humanity that stops wild creatures from interacting with people.

Dogs are trusted and loyal companions that serve as guardians, tracking animals, and pets. Their ability to detect prey or predators via scent and their predilection to accompany humanoids makes them ideal pets for most adventurers. There are hundreds of breeds of dogs in the world—from tiny lapdogs who shower their masters in affection to brawny hounds that stand nearly 4 feet high at the shoulder—and they can be found in nearly any place where people reside. Larger breeds might even be used as mounts for smaller adventurers, and some cultures use dogs as beasts of burden capable of pulling sleds loaded with supplies across the icy tundra. Regardless, many adventurers find value in having a dog.

```statblock
creature: "Guard Dog"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

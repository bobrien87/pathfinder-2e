---
type: creature
group: ["Animal", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cockroach Swarm"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +8, Stealth +8"
abilityMods: ["+2", "+4", "+3", "-5", "+0", "-4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +9, **Ref** +10, **Will** +6"
health:
  - name: HP
    desc: "20; **Immunities** precision, swarm mind; **Weaknesses** area damage 5, splash damage 5; **Resistances** bludgeoning 2, piercing 5, slashing 5"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Swarming Bites"
    desc: "`pf2:1` Each enemy in the swarm's space takes @Damage[1d8[piercing]|options:area-damage] damage (DC 18 [[Reflex]] save)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

While cockroaches tend to gather in cramped spaces, a disturbed colony is sometimes prone to swarming, where hundreds or even thousands of the insects scurry out of their hiding places in a raft of shiny brown and black carapaces on thousands of skittering legs. Given how disgusting many find cockroaches to be, encountering such a swarm can be alarming to even the most seasoned adventurers. The creatures are relentless when disturbed; in contrast to the insects' normally skittish and harmless nature, as swarms they pursue the creature or creatures that provoked them and harry them with thousands of stinging bites.

```statblock
creature: "Cockroach Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

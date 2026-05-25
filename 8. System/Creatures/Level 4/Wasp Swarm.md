---
type: creature
group: ["Animal", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Wasp Swarm"
level: "4"
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
    desc: "+10; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +12"
abilityMods: ["-4", "+4", "+2", "-5", "+2", "-1"]
abilities_top:
  - name: "Wasp Venom"
    desc: "**Saving Throw** DC 21 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison (1 round) <br>  <br> **Stage 2** 2d6 poison and [[Clumsy]] 2 (2 rounds)"
armorclass:
  - name: AC
    desc: "18; **Fort** +10, **Ref** +12, **Will** +8"
health:
  - name: HP
    desc: "45; **Immunities** precision, swarm mind; **Weaknesses** area damage 5, splash damage 5; **Resistances** bludgeoning 7, piercing 7, slashing 3"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Swarming Stings"
    desc: "`pf2:1` Each enemy in the swarm's space takes 2d8 piercing damage (DC 21 [[Reflex]] save). A creature that fails its save is also exposed to wasp venom."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Wasp nests are made of chewed wood fibers foraged from the surrounding flora, which the wasps make into a material similar to paper. A single wasp nest can house thousands of individuals that emerge as a massive swarm. Most swarms attack only to protect their nest or if otherwise agitated, though druids and other primal enchanters can bend these venomous vermin to their will—to deadly effect.

While the common wasp poses little threat to a hardy adventurer aside from an uncomfortable sting, a large and aggressive swarm of these territorial insects—to say nothing of their oversized kin—can lay low an entire party of heroes. The wasps represented here are of the common variety, also known as yellow jackets, but many other sorts of dangerous wasps exist, such as a Garundi variant that swarms in such great numbers that it can decimate entire villages.

```statblock
creature: "Wasp Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

---
type: creature
group: ["Animal", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hippocampus"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +4, Athletics +7"
abilityMods: ["+4", "+1", "+4", "-4", "+3", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +9, **Ref** +4, **Will** +6"
health:
  - name: HP
    desc: "24"
abilities_mid:
  - name: "Buck"
    desc: "`pf2:r` DC 17 [[Reflex]] save <br>  <br> Most monsters that serve as mounts can attempt to buck off unwanted or annoying riders, but most mounts will not use this reaction against a trusted creature unless the mounts are spooked or mistreated. <br>  <br> **Trigger** A creature [[Mounts]] or uses the [[Command an Animal]] action while riding the monster. <br>  <br> **Effect** The triggering creature must succeed at a Reflex saving throw against the listed DC or fall off the creature and land [[Prone]]. If the save is a critical failure, the triggering creature also takes 1d6 bludgeoning damage in addition to the normal damage for the fall."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tail +7 (`pf2:1`) (reach 10 ft.), **Damage** 1d6+4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Sudden Retreat"
    desc: "`pf2:2` The hippocampus makes a tail Strike, then Swims with a +10-foot circumstance bonus to its swim Speed. It gains a +2 circumstance bonus to AC against reactions triggered by this movement."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Hippocampi serve as steeds for aquatic humanoids or roam wild in the sea.

The strange beasts known as hippocampi resemble terrestrial horses from head to midbody, but on their legs, they have splayed fins instead of hooves, and in place of horses' hindquarters, they have powerful tails resembling those of fish. Hippocampi have colorful scales ranging from pearly white to seaweed green, and brilliant ribbed dorsal fins as manes. In the wild oceans, most types of hippocampi tend to congregate in the shallows near the beds of seaweed and kelp forests that provide them with food and shelter from predators. They form huge schools to provide safety in numbers, like landbound horses form herds.

Hippocampi are highly prized by undersea societies and surface dwellers alike, as they are as easy to train as horses and serve many of the same functions, be that as beasts of burden, war-trained mounts, transportation, or as pets. Though hippocampi are able to wear barding, it hampers them considerably, so most handlers outfit them with the lightest options available. More often, they are trained to pull specially designed underwater chariots or sleds. Hippocampi don't like to leave the water, as they are clumsy on land, can't bear riders while flopping about on the ground, and can't breathe air for long.

Numerous variant species of hippocampi exist, although most of them differ from the common hippocampus only in coloration. Heartier species, such as polar hippocampi, dwell exclusively in arctic waters and are best presented as hippocampi with elite adjustments.

```statblock
creature: "Hippocampus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

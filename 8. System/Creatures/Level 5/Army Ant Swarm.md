---
type: creature
group: ["Animal", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Army Ant Swarm"
level: "5"
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
    desc: "+11; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +7"
abilityMods: ["-2", "+4", "+4", "-5", "+2", "-4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "21; **Fort** +13, **Ref** +11, **Will** +9"
health:
  - name: HP
    desc: "55; **Immunities** precision, swarm mind; **Weaknesses** area damage 5, splash damage 5; **Resistances** bludgeoning 2, piercing 5, slashing 5"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
  - name: "Cling"
    desc: "`pf2:r` **Trigger** A creature leaves the swarm's space <br>  <br> **Effect** The swarm takes 1d6 untyped damage as ants cling to the creature and continue biting, dealing 3d6 persistent,piercing damage. High winds or immersion in water reduces the DC of the flat check to end this persistent damage to 5. Any area damage dealt to the creature destroys these clinging ants."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Swarming Bites"
    desc: "`pf2:1` Each enemy in the swarm's space takes @Damage[3d6[piercing]|options:area-damage] damage (DC 21 [[Fortitude]] save). A creature that fails its save against Swarming Bites becomes [[Clumsy]] 1 for 1 round. If the creature attempts a concentrate or manipulate action while affected, it must succeed at a DC 5 flat check or the action is lost; roll the check after spending the action, but before any effects are applied. <br>  <br> > [!danger] Effect: Swarming Bites"
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

An army ant swarm is a terrifying carpet of stinging insects that devours all in its path.

Ants are industrious insects that aid the natural processes of decay and renewal.

```statblock
creature: "Army Ant Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

---
type: creature
group: ["Animal", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Viper Swarm"
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
    desc: "+12; [[Low-Light Vision]], [[Scent]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +13, Stealth +11"
abilityMods: ["+1", "+5", "+3", "-4", "+2", "-3"]
abilities_top:
  - name: "Viper Swarm Venom"
    desc: "**Saving Throw** DC 21 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage (1 round) <br>  <br> **Stage 2** 1d6 poison damage and [[Clumsy]] 1 (1 round) <br>  <br> **Stage 3** 2d4 poison damage, [[Clumsy]] 2, and [[Enfeebled]] 1 (1 round)"
armorclass:
  - name: AC
    desc: "18; **Fort** +11, **Ref** +13, **Will** +10"
health:
  - name: HP
    desc: "50; **Immunities** swarm mind, precision; **Weaknesses** area damage 5, splash damage 5; **Resistances** bludgeoning 5, piercing 5, slashing 3"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Venom Spritz"
    desc: "`pf2:2` The vipers spray venom from their fangs in a defensive display. Each creature in a @Template[type:cone|distance:10] is exposed to viper swarm venom but gains a +2 circumstance bonus to its initial saving throw against the poison."
  - name: "Venomous Fangs"
    desc: "`pf2:1` Each enemy in the swarm's space takes 2d8 piercing damage (DC 21 [[Reflex]] save). A creature that fails their save is also exposed to viper swarm venom."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The frightening mass of shining scales, gleaming eyes, and fangs dripping with venom that constitute a viper swarm has brought an end to many an unlucky adventurer. Normally nocturnal, these notoriously aggressive snakes strike at anything that comes within reach, be it limb or weapon. Their venom is a potent toxin that leaves victims shaky and weak. Those who are lucky may receive a warning strike without venom before being attacked in earnest.

Snakes of some variety thrive in every non-arctic ecosystem, each with their own particular hunting patterns and defense mechanisms.

```statblock
creature: "Viper Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

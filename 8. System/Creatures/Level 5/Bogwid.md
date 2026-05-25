---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bogwid"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +13, Intimidation +11, Stealth +10"
abilityMods: ["+5", "+4", "+4", "-4", "-2", "+1"]
abilities_top:
  - name: "Bogwid Fever"
    desc: "**Saving Throw** DC 20 [[Fortitude]] save <br>  <br> **Onset** 1 day <br>  <br> **Stage 1** [[Enfeebled]] 1 (1 day) <br>  <br> **Stage 2** [[Enfeebled]] 2, and the DC to recover from persistent bleed is increased by 2 (1 day) <br>  <br> **Stage 3** [[Enfeebled]] 3, and the DC to recover from persistent bleed is increased by 5 (1 day) <br>  <br> **Stage 4** [[Enfeebled]] 4, the DC to recover from persistent bleed is increased by 5, and you take 1d8 persistent bleed damage every 1d4 hours (1 day) <br>  <br> > [!danger] Effect: Bogwid Fever"
  - name: "Ravenous Young"
    desc: "The larvae launched from the bogwid attach themselves to the target and begin to feed. Once a larva is attached, the target becomes [[Drained]] 1. While the larva remains attached, the target cannot recover from persistent bleed. To remove the larva, the target can attempt to `act escape dc=21`. Additionally, any area damage dealt to the target destroys all attached larvae. <br>  <br> > [!danger] Effect: Ravenous Young"
armorclass:
  - name: AC
    desc: "20; **Fort** +15, **Ref** +12, **Will** +8"
health:
  - name: HP
    desc: "100; **Weaknesses** cold 5"
abilities_mid:
  - name: "Revolting Aura"
    desc: "20 feet. <br>  <br> A creature entering the aura or begins their turn in the aura must succeed at a DC 20 [[Fortitude]] save or become [[Sickened]] 1 (or [[Sickened]] 2 on a critical failure). A creature that succeeds is temporarily immune to the aura for 1 minute."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tentacle +15 (`pf2:1`) (unarmed), **Damage** 2d8+8 bludgeoning plus [[Bogwid Fever]]"
  - name: "Ranged strike"
    desc: "Larval Spit +14 (`pf2:1`) (range 10 ft.), **Damage** 2d8 bleed plus [[Ravenous Young]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The abhorrent combination between a toad and an octopus, a bogwid drags its bloated green body through the swamps in search of a meal for the many larvae it carries on its back. Despite its absurd appearance and its pervasive scent, a bogwid is an ambush hunter. It will hide itself in sand, vegetation, or whatever happens to be around and wait patiently until a larger creature, such as a humanoid or a crocodile, approaches, before it attacks. A desperate bogwid may even attack a small group in search of food for both it and its young. Once it has a suitably large corpse, the larvae on its back will leap onto it and begin fighting each other for their one chance at survival. The remaining larva buries itself in the body and begins devouring it over the next couple of weeks. Afterward, a fully grown bogwid emerges from what is left of the rotting corpse. Within a week of its new life, the young bogwid too will begin asexually producing larvae on its back, repeating the cycle.

Bogwids earned their name due to their environment. They are almost exclusively found in bogs and swamps. Occasionally one might be found in a suitable warm environment closer to civilization, but they are too often hunted if they are seen near a town or settlement. Some have discovered that bogwids have an extremely negative reaction when introduced to the cold and will violently attack whatever they perceive to be the source.

```statblock
creature: "Bogwid"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

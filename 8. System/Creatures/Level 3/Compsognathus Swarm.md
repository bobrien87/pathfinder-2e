---
type: creature
group: ["Animal", "Dinosaur"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Compsognathus Swarm"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: "Dinosaur"
trait_03: "Swarm"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +9, Stealth +10"
abilityMods: ["+2", "+4", "+2", "+0", "+1", "+0"]
abilities_top:
  - name: "Compsognathus Venom"
    desc: "**Saving Throw** DC 20 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 1d8 poison damage and enfeebled 1 (1 round)"
armorclass:
  - name: AC
    desc: "19; **Fort** +8, **Ref** +12, **Will** +7"
health:
  - name: HP
    desc: "40; **Immunities** grabbed, precision, prone, restrained, swarm mind; **Weaknesses** area damage 5, splash damage 5; **Resistances** bludgeoning 2, piercing 5, slashing 5"
abilities_mid:
  - name: "Evade"
    desc: "`pf2:r` **Trigger** An adjacent enemy targets the swarm with a Strike <br>  <br> **Effect** With quick movements, the swarm gains a +1 circumstance bonus to AC against the triggering attack. If the attack misses, the swarm can Stride up to 10 feet after the Strike."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Venomous Bite"
    desc: "`pf2:1` Each enemy in the swarm's space takes 2d4 piercing damage (DC 20 [[Reflex]] save). A creature who fails the save is also exposed to compsognathus venom."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Though a curious lone compsognathus is occasionally known to sneak into an adventurer's camp, they're often scouting from a nearby pack potentially containing dozens of the tiny bipedal dinosaurs. If the pack is threatened—especially near a nesting site—they'll scurry about in self-defense. Despite their large numbers, the swarm can dart away from danger quickly, and their gnashing teeth carry the threat of venom to anyone who comes too close.

```statblock
creature: "Compsognathus Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

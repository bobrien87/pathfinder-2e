---
type: creature
group: ["Animal", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Jellyfish"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: "Mindless"
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
    desc: "Acrobatics +15, Athletics +17, Stealth +15"
abilityMods: ["+6", "+4", "+6", "-5", "+0", "-5"]
abilities_top:
  - name: "Jellyfish Venom"
    desc: "**Saving Throw** DC 25 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 2d8 poison damage and [[Clumsy]] 1 (1 round) <br>  <br> **Stage 2** 3d6 poison damage and [[Clumsy]] 2 (1 round) <br>  <br> **Stage 3** 2d10 poison damage and [[Paralyzed]] (1 round)"
  - name: "Squeeze"
    desc: "A giant jellyfish can fit into tight spaces as if it were a Medium creature. It can move at its full Speed while [[Squeezing]]."
armorclass:
  - name: AC
    desc: "15; **Fort** +17, **Ref** +15, **Will** +1"
health:
  - name: HP
    desc: "165; **Immunities** critical hits, precision; **Weaknesses** piercing 5, slashing 5; **Resistances** bludgeoning 5, poison 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tentacle +18 (`pf2:1`) (agile, reach 20 ft.), **Damage** 2d8+8 bludgeoning plus [[Jellyfish Venom]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Unlike its smaller cousins, the giant jellyfish is an active predator that chases down its prey through reefs or open water. It can even squeeze its enormous bell-shaped body into the tight confines of shipwrecks to drape its mane of tentacles across the exposed flesh of its prey.

Many varieties of jellyfish drift through the world's oceans, feeding on fish and other tiny marine creatures. However, deadly species of monstrous jellyfish pose a threat to unwary swimmers and sailors alike. Note that while jellyfish are animals, they also have the mindless trait because they lack a centralized nervous system.

```statblock
creature: "Giant Jellyfish"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

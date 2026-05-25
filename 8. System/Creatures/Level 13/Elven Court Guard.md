---
type: creature
group: ["Elf", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Elven Court Guard"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Elf"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+24; [[Low-Light Vision]]"
languages: "Common, Elven, Fey (plus one regional language)"
skills:
  - name: Skills
    desc: "Acrobatics +26, Athletics +23, Intimidation +24, Society +19, Heraldry Lore +21"
abilityMods: ["+4", "+5", "+2", "+2", "+3", "+1"]
abilities_top:
  - name: "Vigilance"
    desc: "A court guard gains a +1 circumstance bonus on Perception checks to `act sense-motive` and `act seek` creatures, and if they succeed, they get a critical success instead."
armorclass:
  - name: AC
    desc: "35; **Fort** +20, **Ref** +27, **Will** +23"
health:
  - name: HP
    desc: "225"
abilities_mid:
  - name: "+1 Status vs. mental effects"
    desc: ""
  - name: "Interposition"
    desc: "`pf2:r` **Trigger** An ally within 15 feet of the guard would take damage <br>  <br> **Effect** The guard Strides. This movement does not trigger reactions, and the guard must end the Stride in a space adjacent to the ally. The guard then switches places with the ally, taking all damage and associated effects instead of the ally."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Elven Curve Blade +27 (`pf2:1`) (finesse, forceful, magical), **Damage** 2d8+12 slashing"
  - name: "Melee strike"
    desc: "Fist +26 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+12 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Longbow +27 (`pf2:1`) (deadly d10, magical, propulsive, reload 0, volley 30, range 100 ft.), **Damage** 2d8+10 piercing"
spellcasting: []
abilities_bot:
  - name: "Avenge the Fallen"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Requirements** The guard is within 30 feet of the creature they were guarding, and that creature is either [[Dying]] or died since the guard's last turn <br>  <br> **Effect** The guard Strikes the creature that damaged their ally. They roll the attack roll twice and use the higher result."
  - name: "Dancing Blade"
    desc: "`pf2:2` The guard makes a Strike against a creature, then Strides. This Stride doesn't trigger reactions. If the guard ends this Stride in a different space adjacent to the same creature, they make another Strike against it. If both Strikes succeed, the creature is [[Off Guard]] until the start of the guard's next turn. Each attack counts toward the guard's multiple attack penalty, but the penalty doesn't increase until they've made both attacks."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

In the tangled web of lineages, rivalries, and shifting alliances that is an elven noble court, aristocratic families employ bodyguards loyal to them alone.

Elves' long lives give them centuries to delve into studies, artistry, or exploration.

```statblock
creature: "Elven Court Guard"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

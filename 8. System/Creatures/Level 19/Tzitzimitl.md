---
type: creature
group: ["Electricity", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tzitzimitl"
level: "19"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Electricity"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+32; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Aklo, Chthonian, Common, Empyrean"
skills:
  - name: Skills
    desc: "Acrobatics +33, Arcana +37, Athletics +33, Nature +37, Occultism +37, Religion +40"
abilityMods: ["+10", "+8", "+6", "+5", "+7", "+8"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Drain Life"
    desc: "When a tzitzimitl's claw Strike deals damage to a living creature, the tzitzimitl gains 20 temporary Hit Points, and the target must succeed at a DC 41 [[Fortitude]] save or become [[Drained]] 2. Further damage dealt by a tzitzimitl's claw Strike increases the value of the drained condition by 2 on a failed save, to a maximum of [[Drained]] 4. <br>  <br> > [!danger] Effect: Drain Life"
armorclass:
  - name: AC
    desc: "43; **Fort** +29, **Ref** +32, **Will** +35"
health:
  - name: HP
    desc: "390; fast healing 15, void healing; **Immunities** bleed, death effects, disease, electricity, paralyzed, poison, unconscious; **Weaknesses** holy 15; **Resistances** cold 15, physical 15 except bludgeoning"
abilities_mid:
  - name: "Fast Healing 15"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Light to Dark"
    desc: "`pf2:r` **Trigger** A creature uses an ability or spell with the vitality trait within 120 feet of the tzitzimitl <br>  <br> **Effect** The tzitzimitl inverts the energy used in the triggering ability or spell, causing it to lose the vitality trait and gain the void trait, and changing all instances of vitality energy or healing in the ability's description to void energy."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +34 (`pf2:1`) (agile, magical, reach 20 ft.), **Damage** 4d12+10 slashing plus 3d8 electricity plus [[Drain Life]]"
  - name: "Ranged strike"
    desc: "Eye Beam +34 (`pf2:1`), **Damage** 4d12 electricity plus 10d6 force"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 0, attack +0<br>**9th** [[Wails of the Damned]]<br>**7th** [[Eclipse Burst]]<br>**6th** [[Teleport]], [[Teleport]], [[Truesight]] (Constant)<br>**3rd** [[Haste]]<br>**2nd** [[Darkness]], [[Darkness]]<br>**1st** [[Detect Magic]]"
abilities_bot:
  - name: "Eclipse"
    desc: "`pf2:2` **Effect** The tzitzimitl casts darkness and drains the heat and warmth from the darkness spell's area. Each creature within the spell's area must attempt a DC 41 [[Fortitude]] save. <br> - **Critical Success** The creature takes 4d8 cold damage. <br> - **Success** The creature takes 8d8 cold damage and is [[Slowed]] 1 for 1 round. <br> - **Failure** The creature takes 16d8 cold damage and is slowed 1 for 1 minute. <br> - **Critical Failure** The creature takes 16d8 cold damage, is [[Slowed]] 2 for 1 minute, and is [[Doomed]] 1."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Due to their affinity for darkness and apocalyptic terror, tzitzimitls are widely feared as harbingers of death and destruction. A solar eclipse marks their arrival, and they draw strange powers of darkness and electricity from these phenomena. Some sages believe tzitzimitls to be instruments of the gods, called down to destroy worlds whose times have come, while others claim they're the undead remains of stranded exiles from a far-off civilization of spacefaring giants. Such legends are ancient and fragmented, but some tell of tzitzimitls being defeated by great heroes and sealed away—though these tales imply that the enormous undead now lie buried and waiting, soon to rampage again should their tombs be breached.

```statblock
creature: "Tzitzimitl"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

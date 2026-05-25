---
type: creature
group: ["Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Calikang"
level: "12"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Humanoid"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Common, Jotun"
skills:
  - name: Skills
    desc: "Athletics +25, Intimidation +24"
abilityMods: ["+7", "+4", "+5", "-2", "+2", "+4"]
abilities_top:
  - name: "Suspended Animation"
    desc: "By concentrating for 5 minutes, the calikang can enter a state of suspended animation, freezing in place and becoming motionless but remaining aware of their surroundings. <br>  <br> While in this state, the calikang gains a +4 status bonus to Fortitude saves; doesn't age; and is immune to disease, inhaled toxins, poison, starvation, and thirst. <br>  <br> The calikang can exit suspended animation as a free action. If they exit this state to attack, the calikang gains a +2 circumstance bonus to their initiative roll."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "31; **Fort** +23, **Ref** +22, **Will** +20"
health:
  - name: HP
    desc: "235; **Immunities** electricity"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Energy Conversion"
    desc: "Whenever the calikang is hit by an electricity spell's attack roll or rolls a successful save against a spell that deals electricity damage, they absorb the energy. <br>  <br> This heals the calikang for an amount of HP equal to quadruple the spell's rank and recharges their Breath Weapon. A calikang can't absorb their own spells this way."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longsword +28 (`pf2:1`) (magical, reach 10 ft., versatile p), **Damage** 2d8+15 slashing"
  - name: "Melee strike"
    desc: "Fist +25 (`pf2:1`) (agile, nonlethal, reach 10 ft., unarmed), **Damage** 3d8+13 bludgeoning"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 28, attack +20<br>**6th** [[Chain Lightning]], [[Truesight]] (Constant)<br>**1st** [[Runic Weapon]] (At Will)"
abilities_bot:
  - name: "Energy Breath"
    desc: "`pf2:2` **Frequency** once per day. <br>  <br> **Effect** The calikang breathes a blast of energy that deals @Damage[13d6[@item.flags.system.rulesSelections.breathWeapon]|options:area-damage] damage to creatures in a @Template[line|distance:60] (DC 28 [[Reflex]] save). The calikang can choose the damage type each time: acid, cold, electricity, fire, or sonic. <br>  <br> Increase the die size to d8 if the calikang chooses electricity."
  - name: "Sixfold Flurry"
    desc: "`pf2:2` The calikang makes up to two longsword Strikes and up to four fist Strikes. Each Strike must be against a different target. <br>  <br> These attacks count toward the calikang's multiple attack penalty, which doesn't increase until after all the attacks are complete. <br>  <br> For 1 round, the calikang gains a circumstance bonus to their AC equal to the number of Strikes they choose not to take, to a maximum of +4 for taking only two Strikes. <br>  <br> > [!danger] Effect: Sixfold Flurry"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Calikangs are giant, blue-skinned, six-armed guardians of ancient tombs and treasuries. They each feel a deep, inherent drive to protect and guard, making them highly sought after as wardens and bodyguards. Because most serve as solitary guardians, few calikang societies exist.

Calikangs' unique physiologies enable them to absorb and manipulate electrical magic as well as other energies. They can live for 200 years-though they can further extend their lives via suspended animation. For this reason, many are chosen to guard tombs or other sealed sites where living guardians would perish and constructs would deteriorate.

```statblock
creature: "Calikang"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

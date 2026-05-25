---
type: creature
group: ["Incorporeal", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "War Wraith"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Wraith"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Darkvision]], [[Lifesense]] (imprecise) 60 feet"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Acrobatics +19, Intimidation +21, Stealth +19"
abilityMods: ["-5", "+6", "+3", "+3", "+4", "+6"]
abilities_top:
  - name: "Void's Embrace"
    desc: "If the victim succeeds at a saving throw against this curse while in sunlight, the curse ends. While a creature has this curse, it bypasses the resistance of the wraith that cursed it <br>  <br> **Saving Throw** DC 28 [[Will]] save <br>  <br> **Stage 1** the victim is [[Dazzled]] in any light (1 hour) <br>  <br> **Stage 2** the victim gains lifesense 30 feet but is [[Blinded]] in any light (1 hour) <br>  <br> **Stage 3** as stage 2, but the creature also has void healing (1 hour) <br>  <br> **Stage 4** the victim becomes [[Unconscious]] and can't awaken (1 day) <br>  <br> **Stage 5** the creature dies and becomes a wraith under the command of the war wraith, its body crumbling to ash"
armorclass:
  - name: AC
    desc: "27; **Fort** +16, **Ref** +19, **Will** +21"
health:
  - name: HP
    desc: "130; void healing; **Immunities** bleed, death effects, disease, paralyzed, poison, precision, unconscious; **Resistances** all damage 10 except force, ghost touch, spirit, vitality"
abilities_mid:
  - name: "Draining Presence"
    desc: "10 feet. A living creature that enters the aura must succeed at a DC 26 [[Fortitude]] save or become [[Drained]] 1. It recovers after it has been out of the aura for 1 minute. A creature that succeeds at its save is temporarily immune to draining presence for 24 hours."
  - name: "Sunlight Powerlessness"
    desc: "While in sunlight, a war wraith is [[Stunned]] 2 and [[Clumsy]] 2."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Wraith Touch +21 (`pf2:1`) (agile, divine, finesse, void), **Damage** 2d12+6 void"
spellcasting: []
abilities_bot:
  - name: "Absorb Wraith"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The war wraith extends their hand toward another wraith creature within 100 feet. The target wraith dissolves and streaks toward the war wraith in a straight line, dealing 3d10 void damage to each creature along the line with a DC 28 [[Fortitude]] save. The war wraith absorbs the essence of the target wraith, becoming [[Quickened]] for 1 minute. They can use their extra action only to Fly or Strike. An unwilling target can resist being absorbed if it succeeds at a DC 28 [[Will]] save."
  - name: "Grip of Fear"
    desc: "`pf2:2` The wraith reaches into an adjacent creature's chest, gripping its heart. The target takes 9d6 mental damage with a DC 28 [[Will]] save. On a critical failure, the creature is also [[Paralyzed]] until the start of the wraith's next turn."
  - name: "Robes of Welcome"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The wraith wraps their robes around an adjacent living creature, exposing it to void's embrace. If any creature is cursed by the wraith's void's embrace, the wraith can't impose void's embrace on another creature."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These menacing spiritual remnants of wicked warlords or bloodthirsty generals are towering specters of shadow and death. Like other wraiths, war wraiths haunt the shadowy places of the world but are more likely to travel greater distances to sow terror or amass influence, often sticking to dark glades or sinister ruins when journeying across sun-dappled lands. War wraiths tend to be arrogant and rarely form a pack with others of their kind, preferring instead to dominate groups of ordinary wraiths. A particularly powerful necromancer might compel packs of war wraiths into service. However, a particularly malevolent goal—such as eradicating a bastion of light and life—might draw several war wraiths together in a common purpose.

War Wraith OriginsNot every war wraith was once an individual. Many of them coalesce over time, merging from multiple wraiths where lost souls accumulate and have their spirits and consciousnesses shorn apart or undermined in some way. These war wraiths tend to think and communicate not as one potent being, but as a riot of voices—often conflicting but truly bone-chilling when they agree to work in unison. In locations where void energy focuses, such as in the Void or on the Isle of Terror, war wraiths form in this way frequently.

```statblock
creature: "War Wraith"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

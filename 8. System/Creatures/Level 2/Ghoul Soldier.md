---
type: creature
group: ["Ghoul", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ghoul Soldier"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Ghoul"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +9, Stealth +8, Survival +6"
abilityMods: ["+3", "+2", "+2", "+1", "+2", "+3"]
abilities_top:
  - name: "Grave Knowledge"
    desc: "+8 skill modifier <br>  <br> **Frequency** once per hour <br>  <br> **Effect** The ghoul calls upon knowledge it retains from one creature it has consumed in the past 7 days. The ghoul attempts a skill check using a skill in which the consumed creature was trained (if it's unclear whether the creature was trained, the GM decides). The ghoul is treated as trained and uses the high skill modifier for the ghoul's level. This takes the same amount of actions or time as usual for the check. <br>  <br> The ghoul can instead automatically learn something specific known by a creature it consumed in the last 7 days, like the location of a [[Hidden]] treasure or the name of a loved one. The ghoul can do this only once for a given creature, no matter how much of its flesh the ghoul consumed."
armorclass:
  - name: AC
    desc: "17; **Fort** +8, **Ref** +8, **Will** +6"
health:
  - name: HP
    desc: "28; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Stench"
    desc: "10 feet. DC 15 [[Fortitude]] save <br>  <br> A creature entering the aura or starting its turn in the area must succeed at a Fortitude save or become [[Sickened]] 1 (plus [[Slowed]] 1 as long as it's sickened on a critical failure). A creature that succeeds at its save or recovers from being sickened is temporarily immune to all stench auras for 1 minute."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +11 (`pf2:1`) (finesse, unarmed), **Damage** 1d10+3 piercing"
  - name: "Melee strike"
    desc: "Claw +11 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d8+3 slashing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Bastard Sword +11 (`pf2:1`) (two hand d12), **Damage** 1d8+3 slashing"
spellcasting: []
abilities_bot:
  - name: "Consume Flesh"
    desc: "`pf2:1` **Requirements** The ghoul is adjacent to the corpse of a creature that died within the last hour. <br>  <br> **Effect** The ghoul devours a chunk of the corpse and regains 2d6 healing Hit Points. <br>  <br> It can regain Hit Points from any given corpse only once."
  - name: "Ghoul Whispers"
    desc: "`pf2:1` **Requirements** A [[Grabbed]], [[Paralyzed]], [[Restrained]], or [[Unconscious]] creature is within the ghoul's reach <br>  <br> **Effect** The ghoul whispers dark thoughts and vile cravings into the creature's ears. The creature must save against the forbidden cravings curse. <br>  <br> **Forbidden Cravings** (curse) A creature can still eat and drink while sickened by this curse <br>  <br> **Saving Throw** DC 18 [[Will]] save <br>  <br> **Stage 1** carrier with no ill effects (1 day) <br>  <br> **Stage 2** 2d6 void damage and the target is [[Sickened]] 1 until it consumes raw meat (1 day) <br>  <br> **Stage 3** as stage 2 <br>  <br> **Stage 4** as stage 2 unless the target has consumed raw meat in the past 24 hours, then it takes 4d6 void damage and is [[Sickened]] 2 until it consumes raw meat; <br>  <br> **Stage 5** if the creature has eaten raw meat in the past 24 hours, it dies and rises as a ghoul, if not, it returns to stage 4"
  - name: "Swift Leap"
    desc: "`pf2:1` The ghoul jumps up to half its Speed. This movement doesn't trigger reactions."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Retaining their martial skill, these powerful ghouls are not afraid to meet their foe in the open, feeding on the flesh of their fallen opponents to learn their combat abilities.

Few creatures are more ubiquitous to sinister locations such as lonely graveyards and ruined crypts than the flesh-eating undead known as ghouls.

```statblock
creature: "Ghoul Soldier"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

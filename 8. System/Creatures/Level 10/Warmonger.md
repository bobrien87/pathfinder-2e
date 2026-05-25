---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Warmonger"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +24, Intimidation +20, Stealth +19, Survival +14, Warfare Lore +21"
abilityMods: ["+6", "+4", "+5", "+1", "+0", "+0"]
abilities_top:
  - name: "War Ready"
    desc: "The warmonger can always roll Warfare Lore for initiative."
armorclass:
  - name: AC
    desc: "29; **Fort** +21, **Ref** +20, **Will** +16"
health:
  - name: HP
    desc: "200"
abilities_mid:
  - name: "Pain Training"
    desc: "The warmonger treats the value of any [[Drained]], [[Dying]], [[Enfeebled]], [[Sickened]], and [[Wounded]] conditions affecting them as 1 lower. The warmonger still has the condition and must remove it normally."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "War Cry"
    desc: "`pf2:r` **Frequency** once per hour <br>  <br> **Trigger** The warmonger critically hits or knocks out an enemy <br>  <br> **Effect** The warmonger screams a battle cry. Each ally in a @Template[type:emanation|distance:30] that hears it deals an additional 1d6 damage with its Strikes for 1 round. <br>  <br> > [!danger] Effect: War Cry"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Battle Axe +23 (`pf2:1`) (magical, sweep), **Damage** 2d8+12 slashing"
  - name: "Melee strike"
    desc: "Fist +22 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+12 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Longbow +21 (`pf2:1`) (deadly d10, magical, propulsive, reload 0, volley 30, range 100 ft.), **Damage** 1d8+9 piercing"
spellcasting: []
abilities_bot:
  - name: "Patch and Set"
    desc: "`pf2:1` **Frequency** once per day <br>  <br> **Requirements** The warmonger has a hand free <br>  <br> **Effect** The warmonger grits their teeth and ties off a wound or sets a bone or joint. They regain 20 healing Hit Points."
  - name: "Power Through"
    desc: "`pf2:2` **Requirements** The warmonger is wielding two melee weapons and isn't [[Fatigued]] <br>  <br> **Effect** The warmonger attempts up to three melee Strikes against different creatures. These count toward the warmonger's multiple attack penalty normally, but the penalty doesn't increase until after all the attacks. The warmonger overexerts themself with the attacks, becoming fatigued. The warmonger can attempt a DC 30 [[Fortitude]] save to recover from this fatigued condition at the start of each of their turns."
  - name: "Sight Prey"
    desc: "`pf2:1` The warmonger singles out one enemy to bring down with ranged attacks until the end of the current turn. The warmonger's ranged Strikes against that creature gain a +1 circumstance bonus to the attack roll and deal an extra 3d6 precision damage. Each time the warmonger hits that creature with a ranged Strike, the creature takes a –10-foot penalty to its Speeds for 1 minute and falls 20 feet if it's flying. <br>  <br> > [!danger] Effect: Sight Prey (Speed Penalty)"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Warmongers believe the base state of life is violence. They stay in peak physical condition with constant training and keep their supplies ready for marching to war.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Warmonger"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

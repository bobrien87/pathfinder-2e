---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Grand Inquisitor"
level: "15"
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
    desc: "+28"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +25, Deception +27, Diplomacy +30, Intimidation +30, Society +28"
abilityMods: ["+5", "+2", "+2", "+3", "+5", "+4"]
abilities_top:
  - name: "+3 to Sense Motive"
    desc: ""
  - name: "Twisting Fear"
    desc: "The grand inquisitor's Strikes deal an extra 3d6 precision damage to [[Frightened]] creatures."
armorclass:
  - name: AC
    desc: "38; **Fort** +26, **Ref** +20, **Will** +28"
health:
  - name: HP
    desc: "215"
abilities_mid:
  - name: "+3 to Reflex vs. Damaging Effects"
    desc: ""
  - name: "Reactive Strike"
    desc: "`pf2:r` If the grand inquisitor's attack hits and this reaction was triggered by a [[Frightened]] creature, the triggering action is disrupted. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Searching Gaze"
    desc: "30 feet. When an opponent ends its turn in the aura, it must attempt a DC 36 [[Will]] save or it becomes [[Frightened]] 1 ([[Frightened]] 2 on a critical failure), and the grand inquisitor learns its surface thoughts (and underlying motive on a critical failure)."
  - name: "Symbol of Loyalty"
    desc: "60 feet. Allies in the aura who are 14th level and lower and are loyal to the grand inquisitor's cause get a +3 status bonus to Will saves."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +30 (`pf2:1`) (forceful, magical, sweep), **Damage** 2d6+15 slashing"
  - name: "Melee strike"
    desc: "Starknife +30 (`pf2:1`) (agile, deadly d6, magical, versatile s), **Damage** 2d4+15 piercing"
  - name: "Melee strike"
    desc: "Starknife +27 (`pf2:1`) (agile, deadly d6, magical, thrown 20, versatile s), **Damage** 2d4+15 piercing"
  - name: "Melee strike"
    desc: "Fist +30 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+15 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Condemn"
    desc: "`pf2:1` The grand inquisitor Demoralizes. On a success, the target is [[Stunned]] with a value equal to its [[Frightened]] condition."
  - name: "I Am the Law!"
    desc: "`pf2:2` The grand inquisitor vows to bring down all the fury of a nation down upon their foes. Up to three lower-level allies within @Template[emanation|distance:60]{60 feet} of the grand inquisitor can use their reaction to [[Grapple]], [[Strike]], or [[Trip]] with a +2 status bonus. <br>  <br> > [!danger] Effect: I Am the Law!"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A grand inquisitor leads powerful governmental forces. They're often champions of oppressive empires or overzealous intelligence networks.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Grand Inquisitor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

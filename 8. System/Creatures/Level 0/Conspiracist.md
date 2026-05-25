---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Conspiracist"
level: "0"
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
    desc: "+8"
languages: "Common"
skills:
  - name: Skills
    desc: "Deception +10, Occultism -1, Performance +10, Society +11, Conspiracy Lore +11"
abilityMods: ["+0", "+2", "+0", "+3", "+0", "+4"]
abilities_top:
  - name: "Compulsive Liar"
    desc: "The conspiracist can use Deception instead of Diplomacy to `act make-an-impression skill=deception` or `act request skill=deception`. Any creature attempting a Perception check to [[Sense Motive]] against the conspiracist gets a result one degree of success worse than they rolled."
  - name: "Social Specialist"
    desc: "For encounters involving deception and social manipulation, the conspiracist is a 4th-level challenge."
armorclass:
  - name: AC
    desc: "14; **Fort** +4, **Ref** +6, **Will** +10"
health:
  - name: HP
    desc: "15"
abilities_mid:
  - name: "Evoke Pity"
    desc: "`pf2:r` **Trigger** An enemy reduces the conspiracist to below half their maximum HP <br>  <br> **Effect** The conspiracist begs their assailants to \"see reason\" and let them live. The conspiracist attempts a single Performance check against the Will DCs of all enemies in a @Template[type:emanation|distance:30]. Any creature the attempt succeeds against takes a –2 circumstance penalty to damaging attacks without the nonlethal trait they make against the conspiracist for 10 minutes"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +4 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Sow Doubt"
    desc: "`pf2:2` The conspiracist argues that their enemies have been hoodwinked into attacking them by nefarious powers. The conspiracist attempts a single [[Deception]] check against the Will DCs of all enemies that can hear them. <br> - **Critical Success** The enemy fully believes the conspiracist, becoming [[Stupefied 2]] for 1 minute. If the creature was already stupefied 2, they become [[Controlled]] by the conspiracist until the end of the encounter. <br> - **Success** The enemy has trouble disbelieving the conspiracist's logic, becoming [[Stupefied 1]] for 1 minute. If they're already stupefied 1, they become stupefied 2. <br> - **Failure** The enemy is unconvinced, but a seed of doubt remains. <br> - **Critical Failure** The enemy sees through the conspiracist's act, becoming immune to Sow Doubt for 24 hours."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Conspiracists misinform and falsify facts to further their own causes. Though they pose little physical threat, conspiracists can have more powerful allies, such as a deluded mob that respond to the conspiracist's signal.

Villains pursue selfish and cruel goals, trampling over anyone in their way.

```statblock
creature: "Conspiracist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

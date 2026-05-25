---
type: creature
group: ["Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Revenant"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Undead"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "any one spoken in life by their murderer (typically Common)"
skills:
  - name: Skills
    desc: "Athletics +15, Intimidation +14"
abilityMods: ["+5", "+3", "+4", "+0", "+3", "+2"]
abilities_top:
  - name: "Sense Murderer"
    desc: "A revenant knows the direction of their murderer (as long as both are on the same plane), but not the distance."
armorclass:
  - name: AC
    desc: "23; **Fort** +14, **Ref** +13, **Will** +17"
health:
  - name: HP
    desc: "115; void healing; **Immunities** bleed, death effects, disease, paralyzed, poison, sleep; **Resistances** physical 5 except slashing"
abilities_mid:
  - name: "Self-Loathing"
    desc: "If a revenant sees their own reflection or any object that was important to them in life, they must attempt a DC 25 [[Will]] save. <br> - **Critical Success** The revenant is unaffected and can no longer be affected by that reflection or object in this way. <br> - **Success** The revenant is distracted by self-loathing and becomes [[Slowed]] 1 for 1 round. <br> - **Failure** The revenant becomes [[Fascinated]] by the source that triggered their self-loathing and does everything they can to destroy it until the end of the revenant's next turn. <br> - **Critical Failure** The revenant becomes [[Immobilized]] as long as the source of their self-loathing is apparent, until they're attacked, or until they see their murderer."
  - name: "Undying Vendetta"
    desc: "If the revenant's murderer dies, the revenant is immediately destroyed. A revenant that can't sense their murderer must attempt a DC 11 flat check once every 24 hours to avoid becoming [[Immobilized]] and [[Prone]]; they immediately rise again once they can sense their murderer. A murderer who becomes undead does not trigger the revenant's destruction until the murderer is finally destroyed. The revenant gains a +2 status bonus to checks and DCs against their murderer."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +17 (`pf2:1`) (agile, unarmed), **Damage** 2d8+5 slashing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Baleful Shriek"
    desc: "`pf2:2` The revenant wails horribly. Each creature within a @Template[burst|distance:60] must attempt a DC 23 [[Will]] save. Regardless of the outcome of their saving throw, affected creatures are then immune to Baleful Shriek for 1 hour. The revenant's murderer never improves their degree of success due to this ability's incapacitation trait. <br>  <br> The revenant can't use Baleful Shriek again for 1d4 rounds. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Frightened]] 2. <br> - **Failure** The creature is frightened 2 and [[Paralyzed]] for 1 round. <br> - **Critical Failure** The creature is [[Frightened]] 3 and paralyzed for 1d4 rounds."
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d6+5)[bludgeoning]], DC 24 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Revenants are obsessed, undead stalkers who arise from their own murders and are driven by only one thing: revenge against their killers. The common wisdom is that revenants arise only from individuals who have been utterly betrayed or abandoned to die a grueling death, but even then, such victims might not rise from their graves. In other cases, revenants might even rise from what might legitimately be considered an accident if the revenant doesn't understand the full circumstances of their demise. In such cases, it doesn't matter that the "murderer" may not have intended to kill, for revenants understands no pity and can never forgive. Revenants have little memory of their lives other than anything they might need to recall in order to achieve their goal of vengeance.

```statblock
creature: "Revenant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Expedition Leader"
level: "9"
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
    desc: "+21"
languages: "Common, Erutaki, Skald, Tien, Varki"
skills:
  - name: Skills
    desc: "Acrobatics +20, Athletics +20, Diplomacy +18, Nature +19, Survival +18, Scouting Lore +21"
abilityMods: ["+4", "+2", "+4", "+2", "+3", "+0"]
abilities_top:
  - name: "Familiarity with the Land"
    desc: "The expedition leader isn't affected by severe weather and ignores difficult terrain."
  - name: "On Guard"
    desc: "When the expedition leader Scouts, they grant their party a +2 circumstance bonus to their initiative rolls. <br>  <br> > [!danger] Effect: On Guard"
armorclass:
  - name: AC
    desc: "27; **Fort** +21, **Ref** +18, **Will** +15"
health:
  - name: HP
    desc: "160"
abilities_mid:
  - name: "Memories of Expeditions Past"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** The expedition leader fails a Survival check <br>  <br> **Effect** The expedition leader rethinks their choices based on prior experience. The degree of success increases by one step, from critical failure to failure or from failure to success."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Machete +21 (`pf2:1`) (deadly d8, magical, sweep), **Damage** 2d6+10 slashing"
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
  - name: "Ranged strike"
    desc: "Shortbow +19 (`pf2:1`) (deadly d10, reload 0, range 60 ft.), **Damage** 1d6+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Quick Draw"
    desc: "`pf2:1` The expedition leader Interacts to take out their machete or shortbow, then Strikes with the weapon."
  - name: "Think Fast!"
    desc: "`pf2:1` **Requirements** The expedition leader has a hand free <br>  <br> **Effect** The expedition leader scoops up a handful of rubble and throws it. Each creature in a @Template[type:cone|distance:15] must succeed at a DC 27 [[Reflex]] save or be [[Dazzled]] and [[Off Guard]] until the start of the expedition leader's next turn."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Full-scale expeditions require a central leader. Expedition leaders tend to have level heads in dangerous situations and can make decisions quickly when time is of the essence.

Explorers are often well-equipped and well-trained for any type of hazard and are eager to lead others into the wild.

```statblock
creature: "Expedition Leader"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

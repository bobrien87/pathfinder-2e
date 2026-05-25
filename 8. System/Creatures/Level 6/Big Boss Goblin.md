---
type: creature
group: ["Goblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Big Boss Goblin"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Goblin"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: "Common, Goblin"
skills:
  - name: Skills
    desc: "Athletics +15, Diplomacy +13, Intimidation +15, Stealth +11"
abilityMods: ["+3", "+1", "+3", "+1", "+1", "+3"]
abilities_top:
  - name: "No Fight Fair"
    desc: "A big boss goblin fights dirty, slashing at a foe's hamstrings. Whenever the big boss goblin hits an [[Off Guard]] foe, the creature takes a –5-foot status penalty to its speed (–10-foot on a critical hit) until the creature regains any amount of Hit Points. As with all penalties to Speed, this can't reduce a creature's Speed below 5 feet. <br>  <br> > [!danger] Effect: No Fight Fair"
armorclass:
  - name: AC
    desc: "22; **Fort** +17, **Ref** +11, **Will** +14"
health:
  - name: HP
    desc: "100"
abilities_mid:
  - name: "Not Me!"
    desc: "`pf2:r` **Trigger** The big boss goblin is targeted with an attack, and a goblin is adjacent to them <br>  <br> **Effect** The big boss goblin yanks the goblin in front of the attack to face the consequences in their stead. The big boss goblin gains a +2 circumstance bonus to their AC against the triggering attack. If it hits, the big boss goblin takes half damage, and the other goblin takes the remaining half."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Horsechopper +17 (`pf2:1`) (magical, reach 10 ft., trip, versatile p), **Damage** 1d8+5 slashing"
  - name: "Melee strike"
    desc: "Jaws +15 (`pf2:1`) (finesse, unarmed), **Damage** 1d6+5 piercing"
  - name: "Ranged strike"
    desc: "Shortbow +14 (`pf2:1`) (deadly d10, reload 0, range 60 ft.), **Damage** 1d6+2 piercing"
spellcasting: []
abilities_bot:
  - name: "Stab it! Stab it! Stab it!"
    desc: "`pf2:1` The big boss goblin picks a target they can see within 30 feet and orders any allied goblins to attack. A single goblin with a lower level than the big boss goblin that is adjacent to the target can immediately use their reaction to Strike the target. In addition, until the start of the big boss goblin's next turn, their attacks against that target deal 1 additional damage dice as the big boss goblin leads them. <br>  <br> > [!danger] Effect: Stab it! Stab it! Stab it!"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Big boss goblins order members of their band around and deal with any longshanks they come across—sometimes via violence or diplomacy, and sometimes by ordering another goblin to deal with them (in ways that the big boss goblin approves of if they work or claims were awful ideas they never would have tried if they don't). These goblin leaders often insist on impressive titles or sobriquets like "The Exceedingly Incendiary," "Snake Singer," or "Most Gluttonest," though these can often be exaggerated by several degrees for dramatic effect or even change at the big boss goblin's whim (often to one-up a rival).

Goblins can be found across Golarion, sometimes threatening taller humanoids (whom they refer to as "longshanks") and sometimes redeeming harmful history by working alongside others.

```statblock
creature: "Big Boss Goblin"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

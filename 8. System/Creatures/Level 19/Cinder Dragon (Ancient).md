---
type: creature
group: ["Dragon", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cinder Dragon (Ancient)"
level: "19"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Dragon"
trait_02: "Fire"
trait_03: "Primal"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+35; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Pyric"
skills:
  - name: Skills
    desc: "Acrobatics +30, Athletics +38, Diplomacy +35, Intimidation +37, Nature +36, Stealth +37"
abilityMods: ["+10", "+4", "+8", "+5", "+6", "+7"]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a cinder dragon's vision; they ignore the [[Concealed]] condition from smoke."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Pyre Breath whenever they score a critical hit with a Strike."
armorclass:
  - name: AC
    desc: "42; **Fort** +34, **Ref** +30, **Will** +32"
health:
  - name: HP
    desc: "425; **Immunities** fire, paralyzed, sleep; **Weaknesses** cold 20"
abilities_mid:
  - name: "+2 Status to All Saves vs. Primal"
    desc: ""
  - name: "Boiling Blood"
    desc: "`pf2:r` **Trigger** The dragon is critically hit with a melee attack <br>  <br> **Effect** The dragon's superheated blood spills onto the attacker. The target takes 10d6 fire damage (DC 41 [[Reflex]] save)."
  - name: "Dragon Heat"
    desc: "5 feet. @Damage[4d6[fire]|options:area-damage] damage (DC 37 [[Reflex]] save)"
  - name: "Frightful Presence"
    desc: "90 feet. DC 39 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Reactive Strike (Jaws only)"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +36 (`pf2:1`) (fire, magical, reach 20 ft.), **Damage** 1d8 fire plus 4d12+12 piercing"
  - name: "Melee strike"
    desc: "Horn +34 (`pf2:1`) (magical, reach 20 ft.), **Damage** 3d12+16 piercing"
  - name: "Melee strike"
    desc: "Claw +36 (`pf2:1`) (agile, magical, reach 15 ft.), **Damage** 4d10+12 slashing"
  - name: "Melee strike"
    desc: "Tail +34 (`pf2:1`) (magical, reach 25 ft.), **Damage** 4d8+12 bludgeoning"
  - name: "Melee strike"
    desc: "Wing +34 (`pf2:1`) (agile, magical, reach 20 ft.), **Damage** 4d8+12 slashing"
spellcasting: []
abilities_bot:
  - name: "All Becomes Flame"
    desc: "`pf2:1` The dragon curses a creature within 60 feet to have its magic replaced with primordial flames. The creature must attempt a DC 39 [[Will]] save. Regardless of the result, the target becomes temporarily immune for 1 day. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is cursed for 1 round. While cursed, any damage the cursed creature would deal by any means becomes fire damage, regardless of the original damage type. The cursed creature can temporarily suppress the curse for 1 round as an action. <br> - **Failure** As success, but the curse's duration is 1 hour. <br> - **Critical Failure** As success, but the curse's duration is 1 day."
  - name: "Draconic Frenzy"
    desc: "`pf2:2` The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Pyre Breath"
    desc: "`pf2:2` The dragon breathes a blast of flame that deals @Damage[18d6[fire]|options:area-damage] damage in a @Template[type:cone|distance:60] (DC 41 [[Reflex]] save). Creatures that critically fail their save catch fire, taking 2d6 persistent,fire damage. The area then fills with black smoke for 1 minute. This has the effects of mist, except it fills the cone's area. The dragon can't use Pyre Breath again for 1d4 rounds."
  - name: "Stoke the Flames"
    desc: "`pf2:1` The dragon intensifies nearby fires. Every foe within 60 feet that is taking persistent fire damage takes 5d6 fire damage."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Among the largest and fiercest dragons, cinder dragons are typically volatile, demanding respect—even deference—from lesser creatures. Cinder dragons' appearance evokes their flame, often in scales with mixed patterns of red, orange, and yellow. Many cinder dragons dwell in active volcanoes and similarly fiery locales. Cinder dragons prefer treasures that can withstand the heat of their bodies and lairs, with gemstones, gold, and silver common among their hoards.

```statblock
creature: "Cinder Dragon (Ancient)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

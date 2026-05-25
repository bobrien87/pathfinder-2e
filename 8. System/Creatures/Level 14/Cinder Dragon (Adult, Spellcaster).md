---
type: creature
group: ["Dragon", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cinder Dragon (Adult, Spellcaster)"
level: "14"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Dragon"
trait_02: "Fire"
trait_03: "Primal"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Pyric"
skills:
  - name: Skills
    desc: "Acrobatics +23, Athletics +29, Diplomacy +25, Intimidation +27, Nature +26, Stealth +23"
abilityMods: ["+8", "+2", "+6", "+3", "+4", "+5"]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a cinder dragon's vision; they ignore the [[Concealed]] condition from smoke."
armorclass:
  - name: AC
    desc: "35; **Fort** +27, **Ref** +23, **Will** +25"
health:
  - name: HP
    desc: "310; **Immunities** fire, paralyzed, sleep; **Weaknesses** cold 15"
abilities_mid:
  - name: "+2 Status to All Saves vs. Primal"
    desc: ""
  - name: "Boiling Blood"
    desc: "`pf2:r` **Trigger** The dragon is critically hit with a melee attack <br>  <br> **Effect** The dragon's superheated blood spills onto the attacker. The target takes 8d6 fire damage (DC 34 [[Reflex]] save)."
  - name: "Dragon Heat"
    desc: "5 feet. @Damage[3d6[fire]|options:area-damage] damage (DC 30 [[Reflex]] save)"
  - name: "Frightful Presence"
    desc: "90 feet. DC 32 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Reactive Strike (Jaws only)"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +29 (`pf2:1`) (fire, magical, reach 15 ft.), **Damage** 1d8 fire plus 3d12+12 piercing"
  - name: "Melee strike"
    desc: "Horn +27 (`pf2:1`) (magical, reach 20 ft.), **Damage** 3d12+16 piercing"
  - name: "Melee strike"
    desc: "Claw +29 (`pf2:1`) (agile, magical, reach 10 ft.), **Damage** 3d10+12 slashing"
  - name: "Melee strike"
    desc: "Tail +27 (`pf2:1`) (magical, reach 20 ft.), **Damage** 3d12+12 bludgeoning"
  - name: "Melee strike"
    desc: "Wing +27 (`pf2:1`) (agile, magical, reach 15 ft.), **Damage** 3d8+12 slashing"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 34, attack +26<br>**6th** (3 slots) [[Cursed Metamorphosis]], [[Truesight]], [[Wall of Fire]]<br>**5th** (3 slots) [[Blazing Bolt]], [[Fireball]], [[Toxic Cloud]]<br>**4th** (3 slots) [[Fire Shield]], [[Mountain Resilience]], [[Wall of Fire]]<br>**3rd** (3 slots) [[Dispel Magic]], [[Haste]]<br>**2nd** (3 slots) [[Floating Flame]], [[Mist]], [[Revealing Light]]<br>**1st** (3 slots) [[Cleanse Cuisine]], [[Fear]], [[Ventriloquism]]<br>**Cantrips** [[Detect Magic]], [[Ignition]], [[Message]], [[Read Aura]], [[Sigil]]"
abilities_bot:
  - name: "Pyre Breath"
    desc: "`pf2:2` The dragon breathes a blast of flame that deals @Damage[13d6[fire]|options:area-damage] damage in a @Template[type:cone|distance:50] (DC 34 [[Reflex]] save). Creatures that critically fail their save catch fire, taking 2d6 persistent,fire damage. The area then fills with black smoke for 1 minute. This has the effects of mist, except it fills the cone's area. The dragon can't use Pyre Breath again for 1d4 rounds."
  - name: "Stoke the Flames"
    desc: "`pf2:1` The dragon intensifies nearby fires. Every foe within 60 feet that is taking persistent fire damage takes 4d6 fire damage."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Among the largest and fiercest dragons, cinder dragons are typically volatile, demanding respect—even deference—from lesser creatures. Cinder dragons' appearance evokes their flame, often in scales with mixed patterns of red, orange, and yellow. Many cinder dragons dwell in active volcanoes and similarly fiery locales. Cinder dragons prefer treasures that can withstand the heat of their bodies and lairs, with gemstones, gold, and silver common among their hoards.

```statblock
creature: "Cinder Dragon (Adult, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

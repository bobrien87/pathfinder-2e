---
type: creature
group: ["Aberration", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vaspercham"
level: "17"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Aberration"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+30; [[Darkvision]], [[See Invisibility]]"
languages: "Aklo"
skills:
  - name: Skills
    desc: "Arcana +33, Athletics +33, Deception +31, Intimidation +29, Sea Lore +33"
abilityMods: ["+8", "+4", "+6", "+8", "+5", "+6"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Hallucinatory Brine"
    desc: "A creature hit by the vaspercham's Strikes or Mindwarping Tide must attempt a DC 38 [[Fortitude]] save. On a failure, the creature is overwhelmed with phantasmal visions, becoming [[Confused]] for 1 round (1 minute on a critical failure)."
armorclass:
  - name: AC
    desc: "41; **Fort** +31, **Ref** +25, **Will** +32"
health:
  - name: HP
    desc: "335; **Weaknesses** fire 15; **Resistances** cold 10, electricity 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Magic-Warping Aura"
    desc: "30 feet. A vaspercham's shell distorts nearby magic. Any creature in the aura who Casts a Spell must attempt a DC 37 [[Will]] save. <br> - **Critical Success** The spell is unaffected, and the caster is temporarily immune to the magic-warping aura for 1 minute. <br> - **Success** The spell is unaffected, but if the spell allows a saving throw, the vaspercham gains a +1 circumstance bonus to save against it. <br> - **Failure** If the spell has a target and there are one or more viable targets within its range, the spell's target changes, determined randomly by the GM. If there's no other possible target within range or the spell has no target, the spell is disrupted. <br> - **Critical Failure** The caster instead Casts another Spell, choosing randomly from their spell repertoire, prepared spells, or available focus spells (as appropriate) and selecting any targets at random."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tentacle +33 (`pf2:1`) (agile, magical, reach 20 ft.), **Damage** 3d10+16 bludgeoning plus [[Hallucinatory Brine]]"
  - name: "Ranged strike"
    desc: "Water Blast +33 (`pf2:1`) (brutal, magical, water, range 100 ft.), **Damage** 2d8+16 bludgeoning plus [[Hallucinatory Brine]]"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 41, attack +33<br>**7th** [[Regenerate]]<br>**6th** [[Spellwrack]]<br>**5th** [[Control Water]] (At Will), [[Howling Blizzard]]<br>**4th** [[Dispelling Globe]]<br>**3rd** [[Lightning Bolt]]<br>**2nd** [[See the Unseen]] (Constant)"
abilities_bot:
  - name: "Mindwarping Tide"
    desc: "`pf2:1` The vaspercham releases an effusion of noxious water from its shell. Creatures within a @Template[type:emanation|distance:15] must save against the vaspercham's hallucinatory brine."
  - name: "Whipping Tentacles"
    desc: "`pf2:2` The vaspercham makes four tentacle Strikes, each against a different target. These attacks count toward the vaspercham's multiple attack penalty, but the multiple attack penalty doesn't increase until after the vaspercham makes all of their attacks."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Vasperchams are aquatic horrors who delight in violence, lurking in the shallows near shorelines. Once a vaspercham settles on a home, they stubbornly stay there, regardless of any communities dwelling nearby. A vaspercham's physical might and magic-warping abilities make them incredibly hard to dislodge once entrenched. Vasperchams respond only to strength, so one must best them in combat to gain their begrudging cooperation. But once a vaspercham recovers their strength, they inevitably betray any temporary alliance.

```statblock
creature: "Vaspercham"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

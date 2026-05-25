---
type: creature
group: ["Arcane", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Rune Dragon (Adult, Spellcaster)"
level: "14"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Arcane"
trait_02: "Dragon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+27; [[Darkvision]], [[Magicsense]] (imprecise) 60 feet, [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic (Seven additional common languages)"
skills:
  - name: Skills
    desc: "Acrobatics +25, Arcana +29, Athletics +27, Crafting +27, Diplomacy +25, Performance +27, Society +25, Survival +25, Linguistics Lore +21, Rune Lore +23"
abilityMods: ["+6", "+6", "+7", "+8", "+6", "+4"]
abilities_top:
  - name: "Magic Sense"
    desc: "The rune dragon is aware of any active magical abilities and effects within the listed range. When the dragon Seeks, it gains the benefits of a 4th-rank detect magic spell within the listed range (in addition to the normal benefits of Seeking)."
  - name: "Runic Scales"
    desc: "The rune dragon's scales function as runestones. The rune dragon can't use the effects or abilities of the runes etched on its scales, but they can transfer these runes to appropriate objects. Transferring a rune to or from an item in this way requires 1 minute, during which the dragon is [[Off Guard]]. The process is automatic and doesn't require a check, but if the dragon stops or is interrupted in this process, the rune is destroyed. A rune dragon can have any number of runes etched on its scales, though they typically have only a handful of runes etched on their scales at a time."
  - name: "Detonating Rune"
    desc: "The rune dragon's Strikes and abilities can leave a detonating rune on their targets. If a creature would receive a detonating rune while they already have one, instead of adding another rune, their current detonating rune activates, dealing 5d6 untyped damage to the target and expending the rune. The detonating rune's damage type matches the dragon's current Shifting Rune. A creature can use an Interact action to remove the rune. Detonating runes fade after 1 minute if not detonated."
armorclass:
  - name: AC
    desc: "36; **Fort** +25, **Ref** +23, **Will** +27"
health:
  - name: HP
    desc: "255; **Immunities** paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Arcane"
    desc: ""
  - name: "Canceling Rune"
    desc: "`pf2:r` **Trigger** The dragon is the target of a spell that requires a saving throw <br>  <br> **Effect** The dragon attempts to unmake the spell's foundational runes. They attempt to counteract the spell (counteract rank 7th, counteract modifier +26). If successful, the dragon is unaffected by the spell; other subjects are affected by the spell normally. The dragon can't use Canceling Rune again for 1d4 rounds."
  - name: "Retributive Rune"
    desc: "`pf2:r` **Trigger** A creature within 15 feet damages the rune dragon <br>  <br> **Effect** With a burst of runic magic, the rune dragon uses their detonating rune ability on the triggering creature and immediately causes the rune to detonate if it didn't automatically do so."
  - name: "Improved Push 10 feet"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Improved Push lists a distance, change the distance the creature is pushed on a success to that distance."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +28 (`pf2:1`) (agile, magical, reach 10 ft.), **Damage** 3d6+14 slashing plus [[Detonating Rune]]"
  - name: "Melee strike"
    desc: "Jaws +28 (`pf2:1`) (magical, reach 15 ft.), **Damage** 3d8+14 piercing plus [[Detonating Rune]]"
  - name: "Melee strike"
    desc: "Tail +26 (`pf2:1`) (magical, reach 20 ft.), **Damage** 3d10+14 bludgeoning plus [[Improved Push]]"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 34, attack +26<br>**6th** (3 slots) [[Chain Lightning]], [[Scrying]], [[Wall of Force]]<br>**5th** (3 slots) [[Howling Blizzard]], [[Imaginary Lockbox]], [[Truespeech]]<br>**4th** (3 slots) [[Dispel Magic]], [[Translate]], [[Wall of Fire]]<br>**3rd** (3 slots) [[Fireball]], [[Gravity Well]], [[Veil of Privacy]]<br>**2nd** (3 slots) [[Blur]], [[Embed Message]], [[Translate]]<br>**1st** (3 slots) [[Alarm]], [[Fear]], [[Gust of Wind]]<br>**Cantrips** [[Detect Magic]], [[Ignition]], [[Message]], [[Sigil]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Entangling Rune"
    desc: "`pf2:1` The rune dragon creates a large trapping rune in a @Template[type:burst|distance:10] within 60 feet. A creature other than the dragon that enters a trapped area or ends their turn in the trapped area activates the rune, causing it to entangle them. That creature must succeed at a DC 34 [[Reflex]] save or become [[Immobilized]] for 1 minute or until it Escapes. The rune can trap only a single creature at a time. The rune vanishes either when a creature succeeds against the rune, when a creature successfully Escapes the rune, or after 1 minute. A creature adjacent to the rune can use an Interact action to remove the rune."
  - name: "Runic Breath"
    desc: "`pf2:2` The dragon launches hundreds of exploding runes that detonate upon impact, dealing @Damage[12d6[untyped]|options:area-damage] damage in a @Template[type:cone|distance:40] (DC 34 [[Reflex]] save). The damage type of this ability is determined by Shifting Rune. Creatures who fail the save are also affected by detonating rune. The dragon can't use Runic Breath again for 1d4 rounds."
  - name: "Shifting Runes"
    desc: "`pf2:1` The rune dragon chooses between acid, cold, electricity, fire, or sonic damage. The runes etched upon the dragon shift, forming runes of that energy on its scales. The dragon gains immunity to that damage type, and their detonating runes and Runic Breath deal that damage type. Anyone trained in Arcana can immediately recognize the energy type of the etched rune without a check."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Rune dragons have an innate insight on the power of runes. Most rune dragons keep a variety of runes etched on their scales, which their bodies can magically empower. They typically don't cast spells themselves, instead relying on their ability to create runes on the fly to produce desired effects. A rune dragon often refers to their hoard as their library, as it's full of important historical texts, plays, speeches, textbooks, and spellbooks written by people of different cultures in a variety of languages. While they can often speak a language with the aid of magic, they much prefer to learn languages in the context of their speakers so they can grasp the nuances hidden within the syntax and the magic within their symbols.

```statblock
creature: "Rune Dragon (Adult, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

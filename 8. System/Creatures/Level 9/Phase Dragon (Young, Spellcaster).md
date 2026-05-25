---
type: creature
group: ["Arcane", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Phase Dragon (Young, Spellcaster)"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Arcane"
trait_02: "Dragon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic"
skills:
  - name: Skills
    desc: "Acrobatics +19, Arcana +20, Athletics +17, Diplomacy +18, Nature +17, Occultism +18, Religion +17, Lore (any two specific locations) +22"
abilityMods: ["+4", "+5", "+3", "+6", "+5", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "27; **Fort** +15, **Ref** +20, **Will** +19"
health:
  - name: HP
    desc: "120; **Immunities** immobilized, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Arcane"
    desc: ""
  - name: "Shoo!"
    desc: "`pf2:r` **Trigger** An enemy within 15 feet damages the dragon <br>  <br> **Effect** The dragon teleports the creature up to 15 feet away. The destination must be on the ground and in a space with no hazards."
  - name: "Unerring Location"
    desc: "The dragon automatically attempts to counteract any teleportation effect that targets them (counteract rank 5th, counteract modifier +20). The dragon can choose to be affected normally instead. Other creatures targeted by the same effect remain affected normally."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d12+8 piercing"
  - name: "Melee strike"
    desc: "Claw +20 (`pf2:1`) (agile, magical), **Damage** 2d8+8 slashing"
  - name: "Melee strike"
    desc: "Tail +18 (`pf2:1`) (magical, reach 15 ft.), **Damage** 2d10+8 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 28, attack +20<br>**4th** (2 slots) [[Liminal Doorway]], [[Unfettered Movement]]<br>**3rd** (3 slots) [[Clairaudience]], [[Haste]], [[Safe Passage]]<br>**2nd** (3 slots) [[Blur]], [[Dispel Magic]], [[Humanoid Form]]<br>**1st** (3 slots) [[Ant Haul]], [[Force Barrage]], [[Tailwind]]<br>**Cantrips** [[Detect Magic]], [[Figment]], [[Message]], [[Read Aura]], [[Telekinetic Projectile]]"
  - name: "Arcane Innate Spells"
    desc: "DC 28, attack +20<br>**4th** [[Flicker]], [[Translocate]], [[Translocate]] (At Will)<br>**1st** [[Detect Magic]], [[Know the Way]], [[Read Aura]]"
abilities_bot:
  - name: "Dislocating Breath"
    desc: "`pf2:2` The dragon exhales a swirl of energy that pulls creatures apart, dealing @Damage[8d6[force]|options:area-damage] damage in a @Template[type:cone|distance:30] (DC 28 [[Reflex]] save). The dragon can teleport any creature that fails its save, teleporting that creature up to 30 feet (or twice as far on a critical failure) in any direction. The destination must be on the ground and in a space with no hazards. The dragon can't use Dislocating Breath again for 1d4 rounds."
  - name: "Phase Jump"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The dragon teleports up to 60 feet. If they are airborne, they maintain their momentum, and do not fall at the end of their turn, even if they didn't use an action to Fly."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

No place can contain a phase dragon or even hold their interest for long; their innate arcane connection ties them to teleportation and repositioning magic. Explorers and scholars, phase dragons move about at will, discovering new locales and the arcane secrets of teleportation. They frequently establish multiple lairs in far-flung places they repeatedly visit. Beyond the typical wealth found in lairs, phase dragons tend to keep items of sentimental value from their travels, such as a particularly rare flower from the region or a piece by a local artist.

```statblock
creature: "Phase Dragon (Young, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

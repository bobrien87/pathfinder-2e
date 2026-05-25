---
type: creature
group: ["Arcane", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Phase Dragon (Adult, Spellcaster)"
level: "13"
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
    desc: "+25; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic"
skills:
  - name: Skills
    desc: "Acrobatics +26, Arcana +27, Athletics +24, Diplomacy +25, Nature +23, Occultism +25, Religion +23, Lore (any three specific locations) +25"
abilityMods: ["+5", "+7", "+3", "+8", "+6", "+5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "33; **Fort** +20, **Ref** +25, **Will** +24"
health:
  - name: HP
    desc: "180; **Immunities** immobilized, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Arcane"
    desc: ""
  - name: "Shoo!"
    desc: "`pf2:r` **Trigger** An enemy within 15 feet damages the dragon <br>  <br> **Effect** The dragon teleports the creature up to 25 feet away. The destination must be on the ground and in a space with no hazards."
  - name: "Unerring Location"
    desc: "The dragon automatically attempts to counteract any teleportation effect that targets them (counteract rank 7th, counteract modifier +25). The dragon can choose to be affected normally instead. Other creatures targeted by the same effect remain affected normally."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +26 (`pf2:1`) (magical, reach 15 ft.), **Damage** 3d12+12 piercing"
  - name: "Melee strike"
    desc: "Claw +26 (`pf2:1`) (agile, magical, reach 10 ft.), **Damage** 3d8+12 slashing"
  - name: "Melee strike"
    desc: "Tail +24 (`pf2:1`) (magical, reach 10 ft.), **Damage** 3d10+12 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 33, attack +25<br>**6th** (2 slots) [[Scrying]], [[Wall of Force]]<br>**5th** (3 slots) [[Banishment]], [[Dispel Magic]], [[Sending]]<br>**4th** (3 slots) [[Liminal Doorway]], [[Unfettered Movement]], [[Mirage]]<br>**3rd** (3 slots) [[Clairaudience]], [[Haste]], [[Safe Passage]]<br>**2nd** (3 slots) [[Blur]], [[Dispel Magic]], [[Humanoid Form]]<br>**1st** (3 slots) [[Ant Haul]], [[Force Barrage]], [[Tailwind]]<br>**Cantrips** [[Detect Magic]], [[Figment]], [[Message]], [[Read Aura]], [[Telekinetic Projectile]]"
  - name: "Arcane Innate Spells"
    desc: "DC 33, attack +25<br>**6th** [[Teleport]]<br>**4th** [[Flicker]], [[Translocate]], [[Translocate]] (At Will)<br>**1st** [[Detect Magic]], [[Know the Way]] (Constant), [[Read Aura]]"
abilities_bot:
  - name: "Dislocating Breath"
    desc: "`pf2:2` The dragon exhales a swirl of energy that pulls creatures apart, dealing @Damage[12d6[force]|options:area-damage] damage in a @Template[type:cone|distance:40] (DC 33 [[Reflex]] save). The dragon can teleport any creature that fails its save, teleporting that creature up to 40 feet (or twice as far on a critical failure) in any direction. The destination must be on the ground and in a space with no hazards. The dragon can't use Dislocating Breath again for 1d4 rounds."
  - name: "Phase Jump"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The dragon teleports up to 75 feet. If they are airborne, they maintain their momentum, and do not fall at the end of their turn, even if they didn't use an action to Fly."
  - name: "Portal Strike"
    desc: "`pf2:2` The dragon momentarily opens a small portal and makes a claw Strike against a creature within 75 feet. The target is [[Off Guard]] to the Strike."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

No place can contain a phase dragon or even hold their interest for long; their innate arcane connection ties them to teleportation and repositioning magic. Explorers and scholars, phase dragons move about at will, discovering new locales and the arcane secrets of teleportation. They frequently establish multiple lairs in far-flung places they repeatedly visit. Beyond the typical wealth found in lairs, phase dragons tend to keep items of sentimental value from their travels, such as a particularly rare flower from the region or a piece by a local artist.

```statblock
creature: "Phase Dragon (Adult, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

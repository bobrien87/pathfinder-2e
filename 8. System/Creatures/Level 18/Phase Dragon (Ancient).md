---
type: creature
group: ["Arcane", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Phase Dragon (Ancient)"
level: "18"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Arcane"
trait_02: "Dragon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+32; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic"
skills:
  - name: Skills
    desc: "Acrobatics +34, Arcana +35, Athletics +32, Diplomacy +33, Nature +31, Occultism +33, Religion +31, Lore (any four specific locations) +33"
abilityMods: ["+6", "+8", "+4", "+9", "+7", "+6"]
abilities_top:
  - name: "Draconic Momentum"
    desc: "Whenever they score a critical hit with a Strike, the dragon chooses to either recharge Dislocating Breath or regain an expended teleportation spell."
armorclass:
  - name: AC
    desc: "41; **Fort** +27, **Ref** +32, **Will** +31"
health:
  - name: HP
    desc: "250; **Immunities** immobilized, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Arcane"
    desc: ""
  - name: "Shoo!"
    desc: "`pf2:r` **Trigger** An enemy within 15 feet damages the dragon <br>  <br> **Effect** The dragon teleports the creature up to 35 feet away. The destination must be on the ground and in a space with no hazards."
  - name: "Unerring Location"
    desc: "The dragon automatically attempts to counteract any teleportation effect that targets them (counteract rank 9th, counteract modifier +32). The dragon can choose to be affected normally instead. Other creatures targeted by the same effect remain affected normally."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +26 (`pf2:1`) (magical, reach 15 ft.), **Damage** 3d12+12 piercing"
  - name: "Melee strike"
    desc: "Claw +26 (`pf2:1`) (agile, magical, reach 10 ft.), **Damage** 3d8+12 slashing"
  - name: "Melee strike"
    desc: "Tail +24 (`pf2:1`) (magical, reach 10 ft.), **Damage** 3d10+12 bludgeoning"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 40, attack +32<br>**8th** [[Quandary]]<br>**7th** [[Interplanar Teleport]], [[Planar Seal]]<br>**6th** [[Teleport]]<br>**4th** [[Flicker]], [[Planar Tether]], [[Translocate]], [[Translocate]] (At Will)<br>**1st** [[Detect Magic]], [[Know the Way]] (Constant), [[Read Aura]]"
abilities_bot:
  - name: "Blinking Barrage"
    desc: "`pf2:3` The dragon channels all their teleportation prowess into a remarkable series of blows. The dragon teleports up to 60 feet to a space adjacent to a creature and makes a claw Strike against that creature. The dragon can do this up to four times, teleporting to a different creature each time. Each attack counts toward their multiple attack penalty, but the penalty does not increase until all attacks have been made. The dragon cannot take actions with the teleportation trait again until the end of their next turn."
  - name: "Dislocating Breath"
    desc: "`pf2:2` The dragon exhales a swirl of energy that pulls creatures apart, dealing @Damage[17d6[force]|options:area-damage] damage in a @Template[type:cone|distance:50] (DC 40 [[Reflex]] save). The dragon can teleport any creature that fails its save, teleporting that creature up to 50 feet (or twice as far on a critical failure) in any direction. The destination must be on the ground and in a space with no hazards. The dragon can't use Dislocating Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "`pf2:2` The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Phase Jump"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The dragon teleports up to 75 feet. If they are airborne, they maintain their momentum, and do not fall at the end of their turn, even if they didn't use an action to Fly."
  - name: "Portal Strike"
    desc: "`pf2:2` The dragon momentarily opens a small portal and makes a claw Strike against a creature within 90 feet. The target is [[Off Guard]] to the Strike."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

No place can contain a phase dragon or even hold their interest for long; their innate arcane connection ties them to teleportation and repositioning magic. Explorers and scholars, phase dragons move about at will, discovering new locales and the arcane secrets of teleportation. They frequently establish multiple lairs in far-flung places they repeatedly visit. Beyond the typical wealth found in lairs, phase dragons tend to keep items of sentimental value from their travels, such as a particularly rare flower from the region or a piece by a local artist.

```statblock
creature: "Phase Dragon (Ancient)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

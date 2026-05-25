---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Watchmage"
level: "5"
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
    desc: "+15"
languages: "Common"
skills:
  - name: Skills
    desc: "Arcana +13, Athletics +10, Intimidation +9, Society +11, Legal Lore +13"
abilityMods: ["+1", "+4", "+2", "+4", "+1", "+0"]
abilities_top:
  - name: "Arcane Watch"
    desc: "The watchmage can either [[Investigate]] or [[Search]] while using the [[Detect Magic]] exploration activity."
  - name: "Eldritch Arms"
    desc: "In a brief ritual that takes 10 minutes, the watchmage chooses a single weapon or unarmed attack through which they can focus their magic. Strikes the watchmage makes with that weapon are magical and deal 1d6 additional force damage."
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +12, **Will** +14"
health:
  - name: HP
    desc: "70"
abilities_mid:
  - name: "Counter Escape"
    desc: "`pf2:r` **Trigger** A creature Casts a Spell with the teleportation trait or as a reaction <br>  <br> **Effect** The watchmage expends a spell slot of the same rank or higher as the trigger creature's spell and attempts to counteract the triggering spell (counteract modifier +11)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +15 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d6+5 bludgeoning"
  - name: "Ranged strike"
    desc: "Shortbow +15 (`pf2:1`) (deadly d10, magical, reload 0, range 60 ft.), **Damage** 1d6+4 piercing"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 20, attack +12<br>**3rd** (2 slots) [[Haste]], [[Slow]]<br>**2nd** (2 slots) [[Dispel Magic]], [[See the Unseen]]<br>**1st** (3 slots) [[Command]], [[Force Barrage]], [[Sure Strike]]<br>**Cantrips** [[Detect Magic]], [[Frostbite]], [[Ignition]], [[Read Aura]], [[Tangle Vine]]"
abilities_bot:
  - name: "Spellbound Strike"
    desc: "`pf2:3` **Requirements** The watchmage is wielding the weapon chosen with Eldritch Arms <br>  <br> **Effect** The watchmage Casts a Spell that takes 1 or 2 actions to cast, imbuing that spell into the weapon. The watchmage Strikes with the required weapon. This counts as two attacks for the watchmage's multiple attack penalty. On a hit, the target is also affected by the spell, though the target gets any normal defenses allowed by the spell. <br>  <br> If the spell is targeted, it targets the creature that was hit and no one else. If the spell is an area, the target must be in the area. A burst is centered on a corner of the target's square if the target is Medium or smaller, or the corner of a square closest to the creature's center if it's Large or larger. A cone or line emits from a square of the watchmage's choice adjacent to the target."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A watchmage uses a mix of magic and martial training to enforce the law. They magically detect invisible criminals, locate stolen property, and counter illegal spells.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Watchmage"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

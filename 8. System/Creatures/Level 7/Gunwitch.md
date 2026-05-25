---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gunwitch"
level: "7"
rare_01: "Rare"
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
    desc: "+13"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +17, Crafting +15, Intimidation +15, Occultism +17, Patron Lore +15"
abilityMods: ["+0", "+4", "+1", "+4", "+2", "+2"]
abilities_top:
  - name: "Firearm Familiar"
    desc: "The gunwitch's firearm acts as their familiar but remains a mindless item with no actions. The master abilities it grants are included in the stat block."
armorclass:
  - name: AC
    desc: "23; **Fort** +12, **Ref** +15, **Will** +15"
health:
  - name: HP
    desc: "90"
abilities_mid:
  - name: "Acrobatic Dodge"
    desc: "`pf2:r` **Trigger** An attacker the gunwitch can observe targets them with an attack <br>  <br> **Effect** The gunwitch gains a +2 circumstance bonus to AC against the triggering attack, and after the attack the gunwitch [[Leaps]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Musket Staff +15 (`pf2:1`) (finesse, magical, two hand d6), **Damage** 1d4+6 bludgeoning plus 1d6 force"
  - name: "Melee strike"
    desc: "Fist +15 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
  - name: "Ranged strike"
    desc: "Musket Staff +18 (`pf2:1`) (concussive, fatal d10, magical, reload 1, range 70 ft.), **Damage** 1d6+6 piercing plus 1d6 force"
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 25, attack +17<br>**4th** (3 slots) [[Confusion]], [[Flicker]], [[Phantom Pain]]<br>**3rd** (3 slots) [[Haste]], [[Paralyze]], [[Slow]]<br>**2nd** (3 slots) [[Invisibility]], [[Telekinetic Maneuver]], [[Telekinetic Maneuver]]<br>**1st** (3 slots) [[Enfeeble]], [[Enfeeble]], [[Sure Strike]]<br>**Cantrips** [[Daze]], [[Detect Magic]], [[Light]], [[Read Aura]], [[Telekinetic Projectile]]"
  - name: "Witch Hex Spells"
    desc: "DC 25, attack +17<br>**1st** [[Needle of Vengeance]], [[Nudge Fate]]"
abilities_bot:
  - name: "Betwitched Shot"
    desc: "`pf2:2` **Requirements** The gunwitch is wielding their firearm familiar and has a hex bullet loaded in it (see Hex Bullet) <br>  <br> **Effect** The gunwitch Casts a Spell that takes 1 or 2 actions to cast into their bullet, then Strikes with their firearm familiar, shooting the magic bullet. This counts as two attacks for the gunwitch's multiple attack penalty. On a hit, the target is also affected by the spell, though the target gets any normal defenses allowed by the spell. <br>  <br> If the spell is targeted, it targets the creature that was hit and no one else. If the spell is an area, the target must be in the area. A burst is centered on a corner of the target's square if the target is Medium or smaller or the corner of a square closest to the creature's center if it's Large or larger. A cone or line emits from a square of the gunwitch's choice adjacent to the target."
  - name: "Bullet Storm"
    desc: "`pf2:2` **Requirements** The gunwitch is wielding their firearm familiar and has a hex bullet loaded into it (see Hex Bullet) <br>  <br> **Effect** The gunwitch unleashes a flurry of projectiles. Each creature in a @Template[type:emanation|distance:60] takes @Damage[8d6[piercing]|options:area-damage] damage with a DC 25 [[Reflex]] save."
  - name: "Hex Bullet"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The gunwitch conjures a magical hex bullet in their firearm. It can be used as a normal bullet or for the Bewitched Shot and Bullet Storm abilities. The bullet vanishes if not fired by the end of the turn."
  - name: "Recall Firearm"
    desc: "`pf2:3` **Frequency** once per day <br>  <br> **Requirements** The gunwitch's firearm familiar is within 1 mile <br>  <br> **Effect** The gunwitch summons their firearm into their hand or hands."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

As wielders of both occult power and firearms, gunwitches pride themselves in using both unconventional weapons and obscure magic. To change their patron ([[Spinner of Threads]]), swap out [[Nudge Fate]] and [[Sure Strike]].

These lone wolves have an aura of mystery, bravado, and swagger.

```statblock
creature: "Gunwitch"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

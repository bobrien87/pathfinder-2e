---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Graveknight Champion"
level: "15"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+27; [[Darkvision]]"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Athletics +31, Intimidation +29, Religion +27, <Deity> Lore +27"
abilityMods: ["+8", "+4", "+5", "+2", "+4", "+6"]
abilities_top:
  - name: "Graveknight's Curse"
    desc: "This curse affects anyone who wears a graveknight's armor for at least 1 hour. <br>  <br> **Saving Throw** DC 40 [[Will]] save <br>  <br> **Onset** 1 hour <br>  <br> **Stage 1** [[Doomed]] 1 and cannot remove the armor (1 day) <br>  <br> **Stage 2** [[Doomed]] 2, speed penalty of -10 feet, and cannot remove the armor (1 day) <br>  <br> **Stage 3** dies and transforms into the armor's graveknight. <br>  <br> > [!danger] Effect: Graveknight's Curse"
  - name: "Ruinous Weapons"
    desc: "Any weapon or unarmed attack the graveknight uses gains the effects of a +1 greater striking weapon and a greater flaming weapon rune."
  - name: "Weapon Master"
    desc: "The graveknight has access to the critical specialization effects of any weapons it wields."
armorclass:
  - name: AC
    desc: "38; **Fort** +28, **Ref** +26, **Will** +25"
health:
  - name: HP
    desc: "275; rejuvenation, void healing; **Immunities** bleed, death effects, disease, fire, paralyzed, poison, unconscious"
abilities_mid:
  - name: "Clutching Armor"
    desc: "`pf2:r` **Trigger** A creature attempts to move away from the graveknight <br>  <br> **Effect** The graveknight's armor animates and attempts to Grab the triggering creature. It makes an Athletics check to [[Grapple]] using the graveknight's Athletics modifier – 2. <br>  <br> The armor can continue to Grapple the creature normally. Since the armor is grappling the creature, the graveknight doesn't need a free hand to do so."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greatpick +30 (`pf2:1`) (fatal d12, fire, magical), **Damage** 3d10+16 piercing"
  - name: "Melee strike"
    desc: "Fist +30 (`pf2:1`) (agile, fire, unarmed), **Damage** 3d6+16 bludgeoning plus 1d6 fire"
  - name: "Ranged strike"
    desc: "Composite Shortbow +28 (`pf2:1`) (deadly d10, fire, magical, reload 0, range 60 ft.), **Damage** 3d6+10 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 33, attack +25<br>**7th** [[Eclipse Burst]], [[Execute]]<br>**5th** [[Divine Immolation]]<br>**3rd** [[Chilling Darkness]], [[Fireball]], [[Fireball]]<br>**2nd** [[Spiritual Armament]]<br>**1st** [[Divine Lance]], [[Light]], [[Shield]], [[Void Warp]]"
abilities_bot:
  - name: "Channel Magic"
    desc: "`pf2:2` The graveknight redirects magical energies through its armor, allowing it to deliver magic through an attack. The graveknight Casts a Spell that takes 1 or 2 actions to cast and requires a spell attack modifier. The effects of the spell don't occur immediately but are imbued into an attack instead. The graveknight then makes a melee Strike with a weapon or unarmed attack. The spell is coupled with the attack, using the attack roll result to determine the effects of both the Strike and the spell. This counts as two attacks for the graveknight's multiple attack penalty but doesn't apply the penalty until after they've completed Channeling Magic. The graveknight can't use Channel Magic again for 1d4 rounds."
  - name: "Devastating Blast"
    desc: "`pf2:2` The graveknight unleashes a @Template[cone|distance:30] of energy. Creatures in the area take @Damage[9d12[fire]|options:area-damage] damage (DC 36 [[Reflex]] save). <br>  <br> The graveknight can use this ability once every 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Once the servant of a deity, the graveknight champion returned as an undead after a life cut short in service to their god.

When a fearsome combatant falls in battle, the warrior's vengeful spirit can sometimes fuse with their armor, creating a graveknight.

```statblock
creature: "Graveknight Champion"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

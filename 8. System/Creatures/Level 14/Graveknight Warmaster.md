---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Graveknight Warmaster"
level: "14"
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
    desc: "+26; [[Darkvision]]"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Athletics +28, Deception +26, Intimidation +28, Religion +24, Society +25, Warfare Lore +27"
abilityMods: ["+8", "+4", "+5", "+3", "+4", "+6"]
abilities_top:
  - name: "Graveknight's Curse"
    desc: "This curse affects anyone who wears a graveknight's armor for at least 1 hour <br>  <br> **Saving Throw** DC 39 [[Will]] save <br>  <br> **Onset** 1 hour <br>  <br> **Stage 1** [[Doomed]] 1 and can't remove armor (1 day) <br>  <br> **Stage 2** [[Doomed]] 2, –10-foot status penalty to Speeds, and can't remove armor (1 day) <br>  <br> **Stage 3** dies and transforms into the armor's graveknight. <br>  <br> > [!danger] Effect: Graveknight's Curse"
  - name: "Ruinous Weapons"
    desc: "Any weapon or unarmed attack the graveknight uses gains the effects of the *+1 greater striking* and *Greater Shock* weapon runes."
  - name: "Weapon Master"
    desc: "The graveknight has access to the critical specialization effects of any weapons it wields."
armorclass:
  - name: AC
    desc: "37; **Fort** +27, **Ref** +24, **Will** +24"
health:
  - name: HP
    desc: "255; void healing, rejuvenation; **Immunities** bleed, death effects, disease, electricity, paralyzed, poison, unconscious"
abilities_mid:
  - name: "Hungry Armor"
    desc: "A creature that Strikes a graveknight warmaster with a melee weapon must succeed at a DC 31 [[Reflex]] save or be disarmed of that weapon. If the creature critically fails, the weapon ends up in the graveknight's space. A creature that hits a graveknight warmaster with an unarmed attack must succeed at a DC 31 [[Reflex]] save or become [[Grabbed]] by the graveknight until the end of its next turn, when it Escapes, or when the graveknight moves, whichever comes first."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Rejuvenation"
    desc: "When a graveknight is destroyed, its armor rebuilds its body over the course of 1d10 days-or more quickly if the armor is worn by a living host. If the body is destroyed before then, the process restarts. <br>  <br> A graveknight can only be permanently destroyed by obliterating its armor (such as with [[Disintegrate]]), transporting it to the Forge of Creation, or throwing it into the heart of a volcano."
  - name: "Sacrilegious Aura"
    desc: "30 feet. When a creature in the aura uses a vitality spell or ability, the graveknight automatically attempts to counteract it, with a +23 counteract modifier."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "War Flail +29 (`pf2:1`) (disarm, electricity, magical, sweep, trip), **Damage** 3d10+14 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +29 (`pf2:1`) (agile, electricity, magical), **Damage** 3d6+14 bludgeoning"
  - name: "Ranged strike"
    desc: "Heavy Crossbow +25 (`pf2:1`) (electricity, magical, reload 2, range 120 ft.), **Damage** 3d10+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Devastating Blast"
    desc: "`pf2:2` The graveknight unleashes a @Template[cone|distance:30] of energy. Creatures in the area take @Damage[8d12[electricity]|options:area-damage] damage (DC 34 [[Reflex]] save). <br>  <br> The graveknight can use this ability once every 1d4 rounds."
  - name: "Exemplar of Violence"
    desc: "`pf2:2` **Frequency** once per round <br>  <br> **Effect** The graveknight attempts a Strike as their armor flashes with sinister power that spurs allies to violence. After the Strike, allies who can see the graveknight can use a reaction to Step or Stride, but they must end this movement in a space adjacent to an enemy. One ally of the graveknight's choice can instead use a reaction to Strike."
  - name: "Phantom Mount"
    desc: "`pf2:3` 7th rank; the steed has AC 34, Fort +23, Ref +20, Will +20, and 85 Hit Points <br>  <br> The graveknight summons a supernatural mount, as [[Marvelous Mount]] heightened to a rank equal to half the graveknight's level. <br>  <br> Unlike marvelous mount, the steed's AC and saving throw bonuses are all 4 lower than the graveknight's, and the steed has one-third the graveknight's Hit Points (rounded down). <br>  <br> If the steed is destroyed, the graveknight must wait 1 hour before using this ability again."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Exemplars of undying violence, graveknight warmasters are devastating forces on the battlefield, able to spur allies to ever greater levels of violence.

When a fearsome combatant falls in battle, the warrior's vengeful spirit can sometimes fuse with their armor, creating a graveknight.

```statblock
creature: "Graveknight Warmaster"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

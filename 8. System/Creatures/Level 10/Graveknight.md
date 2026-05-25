---
type: creature
group: ["Graveknight", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Graveknight"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Graveknight"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Darkvision]]"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Athletics +23, Intimidation +22, Religion +19, Warfare Lore +20"
abilityMods: ["+7", "+4", "+4", "+2", "+3", "+5"]
abilities_top:
  - name: "Graveknight's Curse"
    desc: "This curse affects anyone who wears a graveknight's armor for at least 1 hour <br>  <br> **Saving Throw** DC 33 [[Will]] save <br>  <br> **Onset** 1 hour <br>  <br> **Stage 1** [[Doomed]] 1 and can't remove armor (1 day) <br>  <br> **Stage 2** [[Doomed]] 2, –10-foot status penalty to Speeds, and can't remove armor (1 day) <br>  <br> **Stage 3** dies and transforms into the armor's graveknight."
  - name: "Weapon Master"
    desc: "The graveknight has access to the critical specialization effects of any weapons it wields."
armorclass:
  - name: AC
    desc: "31; **Fort** +21, **Ref** +19, **Will** +18"
health:
  - name: HP
    desc: "175; rejuvenation, void healing; **Immunities** cold, death effects, disease, paralyzed, poison, unconscious, bleed"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Rejuvenation"
    desc: "When a graveknight is destroyed, their armor rebuilds their body over the course of `gmr 1d10` days—or more quickly if the armor is worn by a living host. If the body is destroyed before then, the process restarts. <br>  <br> A graveknight can only be permanently destroyed by obliterating their armor (such as with [[Disintegrate]]), transporting it to the Forge of Creation, or throwing it into the heart of a volcano."
  - name: "Sacrilegious Aura"
    desc: "30 feet. <br>  <br> When a creature in the aura uses a vitality spell or ability, the graveknight automatically attempts to counteract it, with a counteract modifier of +17."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Frost Greatsword +24 (`pf2:1`) (cold, magical, versatile p), **Damage** 2d12+10 slashing plus 1d6 cold"
  - name: "Melee strike"
    desc: "Frost Fist +24 (`pf2:1`) (agile, cold, magical), **Damage** 2d6+10 bludgeoning plus 1d6 cold"
  - name: "Ranged strike"
    desc: "Frost Composite Longbow +21 (`pf2:1`) (cold, deadly d10, magical, propulsive, reload 0, volley 30, range 100 ft.), **Damage** 2d8+6 piercing plus 1d6 cold"
spellcasting: []
abilities_bot:
  - name: "Devastating Blast"
    desc: "`pf2:2` The graveknight unleashes a @Template[cone|distance:30] of energy. Creatures in the area take @Damage[11d6[cold]|options:area-damage] with a DC 29 [[Reflex]] save. <br>  <br> The graveknight can use this ability once every `gmr 1d4 #Recharge Devastating Blast` rounds."
  - name: "Phantom Mount"
    desc: "`pf2:3` HP 58; AC 27, Fort +17, Ref +15, Will +14 <br>  <br> The graveknight summons a supernatural mount, as [[Marvelous Mount]] heightened to a rank equal to half the graveknight's level. Unlike *marvelous mount*, the steed's AC and saving throw bonuses are all 4 lower than the graveknight's, and the steed has one-third the graveknight's Hit Points (rounded down). <br>  <br> If the steed is destroyed, the graveknight must wait 1 hour before using this ability again."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Graveknights are undead warriors granted unlife by a cursed suit of armor.

```statblock
creature: "Graveknight"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

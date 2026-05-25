---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Graveknight Captain"
level: "6"
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
    desc: "+14; [[Darkvision]]"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Athletics +16, Intimidation +15, Survival +12, Warfare Lore +13"
abilityMods: ["+5", "+3", "+4", "+1", "+2", "+3"]
abilities_top:
  - name: "Graveknight's Curse"
    desc: "This curse affects anyone who wears a graveknight's armor for at least 1 hour <br>  <br> **Saving Throw** DC 24 [[Will]] save <br>  <br> **Onset** 1 hour <br>  <br> **Stage 1** [[Doomed]] 1 and can't remove armor (1 day) <br>  <br> **Stage 2** [[Doomed]] 2, –10-foot status penalty to Speeds, and can't remove armor (1 day) <br>  <br> **Stage 3** dies and transforms into the armor's graveknight."
  - name: "Ruinous Weapons"
    desc: "Any weapon or unarmed attack the graveknight uses gains the effects of a +1 striking weapon and a caustic weapon rune."
  - name: "Weapon Master"
    desc: "The graveknight has access to the critical specialization effects of any weapons it wields."
armorclass:
  - name: AC
    desc: "24 26 with shield raised; **Fort** +16, **Ref** +14, **Will** +13"
health:
  - name: HP
    desc: "90; rejuvenation, void healing; **Immunities** acid, bleed, death effects, disease, paralyzed, poison, unconscious"
abilities_mid:
  - name: "Graveknight's Shield"
    desc: "The graveknight's curse extends to their shield, or the graveknight's armor uses a portion of itself to produce a shield. The graveknight has a shield that uses the statistics of a Sturdy Shield of a level no higher than the graveknight's level – 1. The shield is quasi-independent of the graveknight and automatically protects the graveknight from harm. When the shield is raised, it automatically uses [[Shield Block]] to reduce the damage of the first attack against the graveknight each round without the graveknight needing to spend their reaction to do so. The shield automatically rejuvenates with the rest of the graveknight and must be destroyed in the same manner as the graveknight's armor."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Rejuvenation"
    desc: "When a graveknight is destroyed, their armor rebuilds their body over the course of 1d10 days days—or more quickly if the armor is worn by a living host. If the body is destroyed before then, the process restarts. A graveknight can only be permanently destroyed by obliterating their armor (such as with [[Disintegrate]]), transporting it to the Forge of Creation, or throwing it into the heart of a volcano."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Warhammer +16 (`pf2:1`) (acid, magical, shove), **Damage** 2d8+7 bludgeoning plus 1d6 acid"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (acid, agile, unarmed), **Damage** 2d4+7 bludgeoning plus 1d6 acid"
spellcasting: []
abilities_bot:
  - name: "Devastating Blast"
    desc: "`pf2:2` The graveknight unleashes a @Template[cone|distance:30] of energy. Creatures in the area take @Damage[4d12[acid]|options:area-damage] damage (DC 24 [[Reflex]] save). <br>  <br> The graveknight can use this ability once every 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Graveknight captains once proudly led squads of troops in battle.

When a fearsome combatant falls in battle, the warrior's vengeful spirit can sometimes fuse with their armor, creating a graveknight.

```statblock
creature: "Graveknight Captain"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

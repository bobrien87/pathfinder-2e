---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Unrisen"
level: "11"
rare_01: "Common"
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
    desc: "+21; [[Darkvision]], [[Lifesense]] (precise) 30 feet"
languages: "Common (Can't speak any language)"
skills:
  - name: Skills
    desc: "Athletics +24, Stealth +19"
abilityMods: ["+7", "+4", "+5", "-2", "+6", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "28; **Fort** +22, **Ref** +17, **Will** +21"
health:
  - name: HP
    desc: "220; meant to live, void healing; **Immunities** bleed, death effects, disease, paralyzed, poison, unconscious"
abilities_mid:
  - name: "Meant to Live"
    desc: "Whenever an unrisen would take damage from vitality energy, it instead heals half that number of Hit Points."
  - name: "Resurrection Vulnerability"
    desc: "A creature with a prepared or spontaneous spell that can restore the dead to life (such as [[Breath of Life]] or [[Raise Dead]]) can expend an appropriate spell slot as a 2-action activity to destroy an unrisen within 30 feet. The attempt fails if the unrisen succeeds at a Will save against the creature's spell DC."
  - name: "Rise Again"
    desc: "If the unrisen is reduced to 0 Hit Points by means other than fire damage, disintegration, or its resurrection vulnerability, it returns to unlife at the start of its next turn. It has 100 Hit Points and is [[Prone]] in the space in which it was destroyed. The unrisen can't be returned by this ability again for 1 hour."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +24 (`pf2:1`) (deadly d10, magical), **Damage** 3d8+13 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +24 (`pf2:1`) (agile, magical), **Damage** 2d8+13 slashing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Agonized Howl"
    desc: "`pf2:2` The unrisen howls in pain at its cursed existence. Creatures within a @Template[type:emanation|distance:30] take @Damage[9d8[mental]|options:area-damage] damage with a DC 30 [[Will]] save. The unrisen can't use Agonized Howl again for 1d4 rounds."
  - name: "Awful Approach"
    desc: "`pf2:1` **Frequency** once per 10 minutes <br>  <br> **Effect** The unrisen reshapes its grotesque form to move swiftly. It Strides twice. Any living creature that can see the unrisen during this movement must succeed at a DC 28 [[Fortitude]] save or be [[Sickened]] 1 (or [[Sickened]] 2 on a critical failure); this is a mental and visual effect."
  - name: "Death Grip"
    desc: "`pf2:1` **Requirements** The unrisen has a living creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The unrisen attempts to destroy its victim's life force so it shares in the unrisen's fate. The creature must succeed at a DC 30 [[Fortitude]] save or become [[Doomed]] 1. While the curse lasts, the creature regains only half as many HP from effects with both the healing and vitality traits; if it dies, any attempt to raise it from the dead causes it to return as an unrisen. The curse ends automatically if the creature's doomed value is reduced to 0."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

An unrisen is a mangled conglomeration of splintered bones, decaying organs, and rotting flesh, created when a ritual such as resurrect goes catastrophically wrong. Immense care must be taken, for if such a ritual fails utterly, an unrisen can be the result—as many a ritualist has learned to their horror.

Unrisen are barely intelligent, aware only of the agony constantly inflicted by their flawed creation and their resentment for the living. They tend to attack the casters involved in the botched ritual first before lashing out at everyone else around them. Though an unrisen's twisted form is unrecognizable as the intended target of the resurrection, its wordless howls are often disturbingly similar to the deceased's voice. If an unrisen is destroyed before it can rise again, it's reduced to a handful of metallic blue-green salts referred to as essential salts.

```statblock
creature: "Unrisen"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

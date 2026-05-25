---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Necromancer"
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
    desc: "+10"
languages: "Common, Necril"
skills:
  - name: Skills
    desc: "Arcana +11, Intimidation +8, Occultism +13"
abilityMods: ["+2", "+3", "+2", "+4", "+2", "-1"]
abilities_top:
  - name: "Stench of Decay"
    desc: "The necromancer emits a scent of putrid rot in a 5-foot emanation. A living creature that enters or begins its turn in the aura is [[Sickened]] 1."
armorclass:
  - name: AC
    desc: "20; **Fort** +11, **Ref** +12, **Will** +11"
health:
  - name: HP
    desc: "65"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Light Mace +14 (`pf2:1`) (agile, finesse, shove), **Damage** 1d4+8 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 23, attack +15<br>**1st** [[Void Warp]]"
abilities_bot:
  - name: "Undead, Arise!"
    desc: "`pf2:1` The necromancer summons two Medium undead entities in different empty squares up to 30 feet away. These undead entities can take the form of zombies, skeletons, or ghosts, chosen by the necromancer. The entities block movement as though they were creatures and can be attacked. Each entity has 1 Hit Point and the same AC and saves as the necromancer. They can't take actions of their own and deteriorate if the necromancer is reduced to 0 Hit Points. The necromancer can have up to four undead entities at any given time. If they call another, the oldest undead entity deteriorates."
  - name: "Undead, Attack!"
    desc: "`pf2:2` **Requirements** The necromancer has at least one undead entity active <br>  <br> **Effect** The necromancer commands all their undead entities to attack. Each entity can Stride up to 20 feet into an empty square and make a Strike. The Strike has a +15 attack modifier and deals @Damage[2d12[bludgeoning]|traits:magical] damage (or @Damage[2d12[spirit]|traits:magical]{spirit} damage if the entity is a spirit). The Strike has the magical trait, and no multiple attack penalty applies to it."
  - name: "Wave of Death"
    desc: "`pf2:2` **Requirements** The necromancer isn't drained and has at least one undead entity active <br>  <br> **Effect** The necromancer overloads their undead entities with void energy, causing all of them to explode. Each entity is destroyed, dealing @Damage[4d12[void]|options:area-damage] damage to each creature in a @Template[type:emanation|distance:10] with a DC 23 [[Fortitude]] save. A creature in more than one explosion is damaged only once. The necromancer becomes [[Drained]] 1."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Defiling the natural order and spitting in the face of convention, the necromancer remains dutifully committed to understanding what forces await beyond the mortal boundaries of life and death.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

```statblock
creature: "Necromancer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

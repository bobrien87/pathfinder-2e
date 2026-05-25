---
type: creature
group: ["Humanoid", "Ratfolk"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ratfolk Grenadier"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Ratfolk"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Common, Ysoki"
skills:
  - name: Skills
    desc: "Acrobatics +9, Crafting +12, Deception +7, Society +10, Stealth +12, Thievery +9"
abilityMods: ["+0", "+4", "+2", "+4", "+2", "+1"]
abilities_top:
  - name: "Alchemical Grenades"
    desc: "The grenadier carries 6 alchemical grenades that deal either acid, cold, or fire damage plus 2 persistent damage and 2 splash damage of the same type (typically two of each). The grenadier replenishes these each day using scavenged materials."
  - name: "Cheek Pouches"
    desc: "A ratfolk grenadier has stretchy cheek pouches that can store up to 1 cubic foot of objects (though no more than 4 light items). The ratfolk can remove or store an item using the Interact action. As long as the ratfolk has at least one object in their cheek pouches, their speech is noticeably difficult to understand."
  - name: "Swarming"
    desc: "A ratfolk grenadier can end its movement in the same square as an ally that also has this ability. Only two such creatures can share the same space."
armorclass:
  - name: AC
    desc: "21; **Fort** +11, **Ref** +13, **Will** +9"
health:
  - name: HP
    desc: "60"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +12 (`pf2:1`) (agile, finesse), **Damage** 1d4 piercing"
  - name: "Ranged strike"
    desc: "Alchemical Grenade +13 (`pf2:1`) (splash, range 20 ft.), **Damage** 1d6 acid"
  - name: "Ranged strike"
    desc: "Hand Crossbow +12 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6 piercing"
spellcasting: []
abilities_bot:
  - name: "Quick Grenadier"
    desc: "`pf2:1` The ratfolk grenadier draws an alchemical grenade with an Interact action and throws it as a ranged Strike."
  - name: "Quick Stow"
    desc: "`pf2:0` **Frequency** once per round <br>  <br> **Effect** The ratfolk grenadier stores one held item of light or negligible Bulk in its cheek pouches."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Grenadiers use alchemical techniques and stealth to defend their communities.

True to their name, ratfolk are rodent-like humanoids well suited to living on the outskirts of mainstream society. Despite common misconceptions that they are dirty or diseased, ratfolk, or ysoki, as they call themselves, keep impeccably clean. Ratfolk are also sometimes mistaken for wererats and initially treated with fear until they can correct the mistaken identification—if they get the chance to do so.

In general, ratfolk have a keen understanding of pathological and alchemical sciences, which they employ in trade and self-defense. They make accomplished alchemists and inventors, and they often protect their lairs with traps, bombs, and other creations. Ratfolk merchants regularly dispatch large trade caravans that travel widely for a year or more before returning to their home community. During this time, they make an effort to learn new things from the people they encounter and collect interesting materials and goods that they can bring back to their warrens.

In their warrens, on the road, and in cities, ratfolk are extremely communal, thriving on proximity to and contact with one another even in relatively tight spaces. In addition, ratfolk are excellent at fighting in cramped spaces alongside their kin. Threatening one ratfolk or their allies is a surefire way to rally the whole community.

```statblock
creature: "Ratfolk Grenadier"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

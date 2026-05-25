---
type: creature
group: ["Dwarf", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Spirit Priest"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Dwarf"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: "Common, Dwarven, Empyrean, Fey, Petran, Pyric"
skills:
  - name: Skills
    desc: "Athletics +12, Diplomacy +12, Occultism +10, Religion +14, Dwarf Lore +10"
abilityMods: ["+2", "+0", "+3", "+0", "+5", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "19; **Fort** +12, **Ref** +9, **Will** +14"
health:
  - name: HP
    desc: "78"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Clan Dagger +11 (`pf2:1`) (agile, parry, versatile b), **Damage** 1d4+6 piercing"
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 22, attack +14<br>**3rd** (3 slots) [[Safe Passage]]<br>**2nd** (4 slots) [[Augury]], [[Noise Blast]], [[Noise Blast]], [[See the Unseen]], [[Spiritual Armament]]<br>**1st** (4 slots) [[Bless]], [[Detect Magic]], [[Divine Lance]], [[Fear]], [[Guidance]], [[Heal]], [[Infuse Vitality]], [[Shield]], [[Spirit Link]], [[Stabilize]]"
abilities_bot:
  - name: "Spirit's Interference"
    desc: "`pf2:2` The spirit priest calls out to a local spirit to assault the priest's enemies. The spirit unleashes a blast of rocks, attacks with a set of vines, or uses some other appropriate part of the environment to attack all creatures in a @Template[type:burst|distance:10] within 30 feet of the priest. The attack deals @Damage[6d6[bludgeoning]|options:area-damage] damage with a DC 18 [[Reflex]] save. The spirit priest can't use Spirit's Interference for 1d4 rounds. The GM might have this ability deal a different damage type based on the local spirits, such as fire damage when calling on a fire spirit."
  - name: "Spiritual Edge"
    desc: "`pf2:1` The spirit priest aligns their spirit with their magical effects, enhancing the power of their spells. If their next action is to Cast a Spell that deals damage and doesn't have a duration, the spell deals additional spirit damage equal to the spell's rank."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

While dwarves worship gods like most any other ancestry, many dwarves also look to the spirits of the world for guidance and support. Most every object and environment in the world, from a simple rock to an expansive river to the largest of mountains, contains some kind of spirit. Dwarven spirit priests learn how to communicate with these spirits. This spiritual attunement allows these priests to use magic, as well as call on these spirits in times of need.

From the dwarven perspective, most things in life are best done correctly, and that means taking one's time. Dwarves are a focused and intentional people, taking years or even decades to ply their trades, doing their best to make every detail perfect. The patience and dedication required for such tasks pays off, and many dwarves become experts in their respective field, trade, or area of focus. Many dwarves uphold traditions, and since dwarven origins trace back to underground life, many still hone skills focused on life underground.

```statblock
creature: "Spirit Priest"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

---
type: creature
group: ["Caligni", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Caligni Dancer"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Caligni"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Greater Darkvision]]"
languages: "Caligni"
skills:
  - name: Skills
    desc: "Acrobatics +7, Diplomacy +8, Performance +6, Stealth +7, Thievery +7"
abilityMods: ["+0", "+4", "+2", "-1", "+1", "+3"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The caligni dancer deals 1d6 extra precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +9, **Will** +4"
health:
  - name: HP
    desc: "18; final dance"
abilities_mid:
  - name: "Distracting Frolic"
    desc: "`pf2:r` **Trigger** An ally within 10 feet of the dancer rolls a saving throw against a mental or illusion effect <br>  <br> **Effect** The target ally can roll the save twice and take the better result. <br>  <br> > [!danger] Effect: Distracting Frolic"
  - name: "Final Dance"
    desc: "When the dancer dies, their body dissolves into a swirling mass of darkness and light. All creatures in a @Template[emanation|distance:10] must succeed at a DC 17 [[Will]] save or be [[Dazzled]] for 1d4 rounds. <br>  <br> The dancer's possessions are left in a pile where they died."
  - name: "Light Blindness"
    desc: "When first exposed to bright light, the monster is [[Blinded]] until the end of its next turn. After this exposure, light doesn't blind the monster again until after it spends 1 hour in darkness. However, as long as the monster is in an area of bright light, it's [[Dazzled]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Baton +9 (`pf2:1`) (agile, finesse, shove), **Damage** 1d4 bludgeoning"
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4 piercing"
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4 piercing"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 16, attack +8<br>**1st** [[Counter Performance (Visual Only)]], [[Courageous Anthem]]"
abilities_bot:
  - name: "Dancer's Curse"
    desc: "`pf2:1` The caligni dancer touches a foe and curses it. <br>  <br> If the target fails a DC 18 [[Will]] save, it gains [[Clumsy]] 1 and [[Stupefied 1]]. <br>  <br> The target is then temporarily immune for 24 hours. <br>  <br> These conditions persist until the curse is removed. The victim can attempt a new DC 18 [[Will]] save once per hour to end the curse."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Caligni dancers serve as intermediaries between caligni factions, carrying messages and negotiating deals between the notoriously independent groups. Although physically fragile, the dancers serve an important role within caligni society and are rarely seen without guards.

Calignis lurk in subterranean cities, with each caligni growing into a specific role and form determined by supernatural influences in caligni society. Regardless of their size or role, all calignis are gaunt, with pale flesh and white eyes. Many relish the chance to creep above ground at night to steal resources, shadow their surface counterparts, or simply make mischief.

```statblock
creature: "Caligni Dancer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

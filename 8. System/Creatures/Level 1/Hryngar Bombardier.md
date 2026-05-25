---
type: creature
group: ["Duergar", "Dwarf"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hryngar Bombardier"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Duergar"
trait_02: "Dwarf"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4; [[Darkvision]]"
languages: "Common, Dwarven, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +6, Crafting +6, Occultism +6, Stealth +6, Survival +4"
abilityMods: ["+1", "+3", "+2", "+3", "+1", "-1"]
abilities_top:
  - name: "Alchemical Grenades"
    desc: "A hryngar bombardier carries 6 alchemical grenades that deal either acid, cold, or fire damage plus 1 persistent damage and 1 splash damage of the same type (typically two of each). The bombardier replenishes these grenades each day using easily collected materials."
armorclass:
  - name: AC
    desc: "18; **Fort** +7, **Ref** +8, **Will** +4"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "+2 Status to All Saves vs. Magic"
    desc: ""
  - name: "Light Blindness"
    desc: "When first exposed to bright light, the monster is [[Blinded]] until the end of its next turn. After this exposure, light doesn't blind the monster again until after it spends 1 hour in darkness. However, as long as the monster is in an area of bright light, it's [[Dazzled]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Warhammer +4 (`pf2:1`) (shove), **Damage** 1d8+1 bludgeoning"
  - name: "Ranged strike"
    desc: "Alchemical Grenade +8 (`pf2:1`) (splash, range 20 ft.), **Damage** 1d6 acid"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 17, attack +9<br>**2nd** [[Blood Vendetta]], [[Paranoia]]<br>**1st** [[Sigil]]"
abilities_bot:
  - name: "Quick Bombardier"
    desc: "`pf2:1` The hryngar bombardier draws an alchemical grenade with an Interact action and throws it as a ranged Strike."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Hryngar chemists have a knack for creating alchemical grenades. Their traditions often motivate them to constantly experiment and innovate, though the hostile nature of their environs tends to focus these innovations on weapons or other tools of war. Hryngar bombardiers eagerly steal notes and secrets from their underlings, pushing their students to cut corners to produce results while gleefully pillaging the credit and profits. For those hryngar bombardiers who find themselves pressed into combat service, each thrown grenade represents a new opportunity to observe the suffering they inflict, before eagerly incorporating that data into their next experiment or innovation to create an even more terrible tool of torment.

Deep beneath the surface, the dour dwarves known as hryngars stubbornly toil, claiming the ancestral subterranean homelands of other dwarves as their own. Long ago, hryngar leaders refused to venture to the surface along with their "cousins," forsaking the Quest for Sky. An exiled dwarven deity named Droskar offered hryngars salvation from the horrors that beset them in the Darklands, offering them power, cunning, and knowledge in exchange for their unending servitude. Many hryngar believe that by working harder than their brethren, they can build a society far greater than anything under the sun, claiming unending riches from the planet's metallic veins in days of relentless toil.

Through Droskar's blessings and their own fearsome work ethic, hryngar kingdoms now rule a significant portion of the upper Darklands region of NarVoth, and it's common to see hryngar caravans moving through the tunnels, drawn by teams of immense beetles. Hryngar leadership typically consists of powerful divine servants of Droskar, along with fearsomely implacable warriors whose martial prowess, backed by innate occult magic, ensures they can overcome any direct threat to hryngar rule. Almost every aspect of hryngar society is controlled by a strict hierarchy of leadership, with taskmasters directing subordinates across all walks of life.

```statblock
creature: "Hryngar Bombardier"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

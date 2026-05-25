---
type: creature
group: ["Mummy", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mummy Guardian"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Mummy"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: "Necril (plus any one language they knew while alive)"
skills:
  - name: Skills
    desc: "Athletics +15, Stealth +11"
abilityMods: ["+4", "+0", "+2", "-2", "+4", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "23; **Fort** +14, **Ref** +10, **Will** +16"
health:
  - name: HP
    desc: "125; void healing; **Immunities** bleed, death effects, disease, paralyzed, poison, unconscious; **Weaknesses** fire 5, alchemical 5"
abilities_mid:
  - name: "Alchemical Weakness"
    desc: "The guardian's weakness to alchemical items not only applies to damage from alchemical items, but the guardian also takes 5 damage when splashed with non-damaging alchemical items or dosed with alchemical poisons, even if they're immune to their other effects."
  - name: "Blighted Consumption"
    desc: "`pf2:r` **Trigger** A creature within 30 feet eats or drinks (including an alchemical item or potion) <br>  <br> **Effect** The food or drink burns like the caustic substances fed to the mummy before its death. If the creature fails a DC 24 [[Fortitude]] save, they become [[Sickened]] 2 after they finish the consumption and can't reduce their sickened condition while within 30 feet of any mummy."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, unarmed), **Damage** 2d10+7 bludgeoning plus [[Choking Pain]]"
spellcasting: []
abilities_bot:
  - name: "Choking Pain"
    desc: "`pf2:1` **Requirements** The mummy's last action was a successful fist Strike <br>  <br> **Effect** The mummy shares the pain of its dying moments with the target of that Strike. That creature takes 3d8 void damage with a DC 24 [[Will]] save. If the creature critically fails the saving throw, it can't speak for 1 round, including to Cast a Spell."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The majority of mummy guardians were created by cruel and selfish masters to serve as guardians to protect their tombs from intruders. The traditional method of creating a mummy guardian is a laborious and sadistic process that begins well before the poor soul to be transformed is dead. The victim is ritualistically starved of nourishing food and instead fed strange spices, preservative agents, and toxins intended to quicken the desiccation of the flesh. The victim remains immobile but painfully aware during the final stages, as its now-useless entrails are extracted. The victim is then shrouded in funerary wrappings and entombed within a necromantically ensorcelled sarcophagus to await instructions in the potentially distant future. While it's certainly possible to use other methods to create a mummy guardian from an already-deceased body, those who seek to create these foul undead as their guardians in the afterlife often feel that such methods result in inferior undead—the pain and agony of death by mummification being an essential step in the process.

Regardless of the method of their creation, mummy guardians are more than just physical shells of flesh and bone. They retain fragmented, distorted versions of their minds, with only enough memories of their living personality remaining to fuel their undead anger and jealousy of those who yet live. This burning rage only intensifies over the centuries of waiting within a crypt for the chance to actually act, and thus, when most mummy guardians are awoken by tomb robbers or adventurers, they stop at nothing in pursuit of spiteful slaughter.

While many cultures practice mummification for benign reasons, undead mummies are created through grueling rituals, typically to provide eternally vigilant guardians. Much more rarely, a body mummified without those special rites can rise again due to its hatred of the living.

```statblock
creature: "Mummy Guardian"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

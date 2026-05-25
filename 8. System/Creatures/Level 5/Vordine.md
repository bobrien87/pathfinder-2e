---
type: creature
group: ["Devil", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vordine"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Greater Darkvision]]"
languages: "Common, Diabolic (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +15, Intimidation +13, Religion +12, Warfare Lore +13"
abilityMods: ["+4", "+4", "+5", "+2", "+3", "+2"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "22; **Fort** +14, **Ref** +13, **Will** +10"
health:
  - name: HP
    desc: "60; **Immunities** fire; **Weaknesses** holy 5; **Resistances** physical 5 except silver, poison 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Trident +15 (`pf2:1`) (magical, unholy), **Damage** 1d8+10 piercing"
  - name: "Melee strike"
    desc: "Whip +15 (`pf2:1`) (disarm, finesse, magical, nonlethal, reach 10 ft., trip, unholy), **Damage** 1d4+10 bludgeoning"
  - name: "Melee strike"
    desc: "Hoof +15 (`pf2:1`) (agile, magical, unholy), **Damage** 1d4+7 bludgeoning plus 1d4 fire"
  - name: "Melee strike"
    desc: "Trident +13 (`pf2:1`) (magical, thrown 20, unholy), **Damage** 1d8+10 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 19, attack +11<br>**4th** [[Translocate]] (At Will)"
abilities_bot:
  - name: "Burning Hoofprints"
    desc: "`pf2:2` The vordine Strides, trailing hoofprints in each square they exit. The hoofprints burn for 1 minute. A creature on the ground that enters a square with burning hoofprints or begins its turn in one takes 1d4 fire damage."
  - name: "Trident of Dis"
    desc: "`pf2:1` The vordine makes a trident Strike, increasing their reach to 10 feet for that Strike. If there is an unholy ally between the vordine and their target, that creature's energy causes the Strike to deal an additional 1d6 spirit damage."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The vast city of Dis trains endless legions of vordines to guard the upper layers of Hell and march across the planes at the archdevils' orders. Although quick to bend their knees to higher-ranking devils and even mortals favored by Asmodeus, vordines are relentlessly cruel to orts and other devils they can call their subordinates.

Although higher ranks in the infernal military are held by more powerful devils, like the nessari who serve as generals, a labyrinthine structure gives each vordine a rank and certain responsibilities. Some vordines are responsible for the battlefield command of squads, while others relay orders from above or are set to handling specific administrative tasks for their unit. The greatest gift one can offer a vordine is an increased rank to lord over other vordines.

Masters of corruption and architects of conquest, devils seek both to tempt mortal life to join in their pursuit of all things profane and to spread tyranny throughout all worlds. The temptations they offer mortals range from great powers granted by the signing of an infernal contract to twisted favors following a whispered pledge to a diabolic patron, or any number of even subtler exchanges. Those who succumb to these temptations find themselves consigned to an afterlife of endless torment in the pits of Hell, wherein the only hope of escape lies in the chance of being promoted to become a devil in the infernal ranks.

Every devil has a specific role to play in the upkeep of the remorseless bureaucratic machine that is Hell, from soldiers and scholars to inquisitors, lawyers, judges, and executioners. Lowly orts perform subservient labor to more powerful and specialized devils, such as infantry and contract devils, while the greatest nessaris command entire infernal armies.

Asmodeus stands at the apex of the structure he created, but the layers below him are marked by a constant jockeying for position. Most diabolic plans ultimately serve to improve the schemer's place in the hierarchy.

```statblock
creature: "Vordine"
```

**Source:** `= this.sourcebook` (`= this.source-type`)

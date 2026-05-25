---
type: background
source-type: "Remaster"
boosts: "Cha/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Library Lore Lore"
source: "Pathfinder Revenge of the Runelords Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

While you've already made a name for yourself as a hero, either here in the Saga Lands or further abroad, adventuring has been in your blood from the very start. Someone closely related to you—perhaps a parent, sibling, cousin, aunt, or uncle, was part of a group of adventurers who they clashed against a runelord-themed villain. This could even be a previous PC you or another player played at your table in a previous Adventure Path like Rise of the Runelords, Shattered Star, or Return of the Runelords—or in a standalone adventure or Organized Play scenario. Work with the other players and the GM as needed to forge these family links, or you can simply be related to a hero from an unplayed adventure. If you choose this route, you can even create (with the GM's aid) this unplayed runelord-themed story. Regardless of the nature of your relationship, it's inspired or pursued you your entire life. Whether you grew up as a privileged young adventurer, tried your hardest to distance yourself from your relation's fame, or are proud of their accomplishments while working hard to move beyond your relation's heroic shadow, you've certainly found that adventuring and heroics appeal to your mind and soul. You may have big shoes to fill, but so far, you've more than risen to the challenge. Enough to draw Queen Sorshen's attention—in her invitation for you to attend the opening ceremony of the Circle of Open Hands, she mentioned that while she first took notice of you after learning of your relative, she's been impressed with your accomplishments and notes that she expects you to exceed your forebear's triumphs. While she expressed curiosity about an "inside view" of some of your relation's accomplishments, she was more eager to meet you as, in her words, "a promising new hero who might just soon change the world."

Choose two attribute boosts. One must be to **Charisma** or **Strength**, and the other is a free attribute boost.

You're trained in Athletics and Library Lore. The disconnect between physical accomplishments and scholastic accomplishments has never been a particular challenge for you, and while this has caused jealousy now and then with childhood friends and rivals, you've managed to hone your skills so that regardless of who you're talking to, your knack of being able to find a common ground has made it easy to make a good impression. Whenever you take part in an influence encounter to Discover or Influence, or attempt to `act make-an-impression` on an NPC, you reduce the DC of those checks by 2.

**Source:** `= this.source` (`= this.source-type`)
